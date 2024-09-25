from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import desc
import os

from looger import logger
from model import *
from schemas import *


info = Info(title="Machine Learning HR Recruitment Prediction", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

doc_tag = Tag(
    name="Documentation", description="API documentation with Swagger, Redoc or RapiDoc"
)
candidate_tag = Tag(
    name="Candidate",
    description="Create, Read, Update, Delete Candidates and Predict hiring decision.",
)


@app.get("/", tags=[doc_tag])
def home():
    """Redirect to openapi documentation with Swagger, Redoc or Rapidoc."""

    return redirect("/openapi")


@app.get(
    "/candidate",
    tags=[candidate_tag],
    responses={"200": ListCandidatesSchema},
)
def get_all_candidates():
    """List all candidates in the database by descend order of the updated_at attribute.
    Args:
       none

    Returns:
        candidates: list of candidates or empty list
    """
    logger.debug("Coletando dados sobre todos os candidatos")

    session = Session()
    candidates = session.query(Candidate).order_by(desc(Candidate.updated_at)).all()

    if not candidates:

        return {"candidates": []}, 200
    else:
        logger.debug(f"%d candidatos econtrados" % len(candidates))

        return format_all_candidates(candidates), 200


@app.post(
    "/candidate",
    tags=[candidate_tag],
    responses={"200": CadidateViewSchema, "400": ErrorSchema, "409": ErrorSchema},
)
def predict(form: CandidateSchema):
    """Insert or Update candidate to the database.
    Use the machine learning model to predict the data for Hiring Decision before insert or update.


    Args:
        email: str
        age: int
        gender: int
        education_level: int
        xp_years: int
        prev_cia_worked: int
        dist_cia: float
        interview_score: int
        skill_score: int
        personality_score: int
        recruitment_strategy: int
        is_update: bool = None

    Returns:
        dict: Candidate representation with the Hiring decision data included
    """
    # Connect to databse and verify if candidate exists
    session = Session()
    candidate_query = session.query(Candidate).filter(Candidate.email == form.email)

    # Get boolean to update candidate data
    is_update = form.is_update

    if candidate_query.count() > 0 and not is_update:
        error_msg = (
            "Candidato já existente na base. Para Update selecionar checkbox indicado."
        )
        logger.warning(f"Erro ao adicionar candidato '{form.email}', {error_msg}")
        return {"message": error_msg}, 409

    # Get data from the request form
    email = form.email
    age = form.age
    gender = form.gender
    education_level = form.education_level
    xp_years = form.xp_years
    prev_cia_worked = form.prev_cia_worked
    dist_cia = form.dist_cia
    interview_score = form.interview_score
    skill_score = form.skill_score
    personality_score = form.personality_score
    recruitment_strategy = form.recruitment_strategy

    # Preprocess data from the request form
    X_input = PreProcessor.set_form(form)

    # Load the pipeline
    pipeline_path = os.path.join(
        "machine_learning", "pipelines", "hr_recruitment_GBpipeline.pkl"
    )
    pipeline = Pipeline.load_pipeline(pipeline_path)

    # Predict the Hiring Decision Data
    hiring_decision = int(MLmodel.predictor(pipeline, X_input)[0])

    logger.debug(f"Adicionando candidate de email: '{email}'")
    try:
        # Update candidate data or insert a new one
        if is_update and candidate_query.count() > 0:
            candidate_query.update(
                {
                    Candidate.age: age,
                    Candidate.gender: gender,
                    Candidate.education_level: education_level,
                    Candidate.xp_years: xp_years,
                    Candidate.prev_cia_worked: prev_cia_worked,
                    Candidate.dist_cia: dist_cia,
                    Candidate.interview_score: interview_score,
                    Candidate.skill_score: skill_score,
                    Candidate.personality_score: personality_score,
                    Candidate.recruitment_strategy: recruitment_strategy,
                    Candidate.hiring_decision: hiring_decision,
                    Candidate.updated_at: datetime.now(),
                }
            )
            session.flush()
            candidate = candidate_query.first()
        else:
            candidate = Candidate(
                email=email,
                age=age,
                gender=gender,
                education_level=education_level,
                xp_years=xp_years,
                prev_cia_worked=prev_cia_worked,
                dist_cia=dist_cia,
                interview_score=interview_score,
                skill_score=skill_score,
                personality_score=personality_score,
                recruitment_strategy=recruitment_strategy,
                hiring_decision=hiring_decision,
                updated_at=datetime.now(),
            )
            session.add(candidate)

        # Commit transation
        session.commit()
        logger.debug(f"Adicionado candidato de email: '{email}'")

        return format_candidate(candidate), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo item."
        logger.warning(f"Erro ao adicionar candidato '{email}', {error_msg}")
        return {"message": error_msg}, 400


@app.delete(
    "/candidate/<id>",
    tags=[candidate_tag],
    responses={"200": CadidateViewSchema, "404": ErrorSchema},
)
def delete_candidate(path: CandidateIdSchema):
    """Remove a candidate form the database.

    Path parameter:
        id (int): candidate id

    Returns:
        message: success or failure
    """

    candidate_id = path.id
    logger.debug(f"Deletando dados sobre candidato #{candidate_id}")

    session = Session()

    candidate = session.query(Candidate).filter(Candidate.id == candidate_id).first()

    if not candidate:
        error_msg = "Candidato não encontrado na base :/"
        logger.warning(f"Erro ao deletar candidato '{candidate_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(candidate)
        session.commit()
        logger.debug(f"Deletado candidato #{candidate_id}")
        return {"message": f"Candidato {candidate_id} removido com sucesso!"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
