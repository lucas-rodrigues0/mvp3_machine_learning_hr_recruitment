from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from urllib.parse import unquote

from looger import logger
from model import *
from schemas import *


info = Info(title="Machine Learning HR Recruitment Prediction", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentation", description="API documentation with Swagger, Redoc or RapiDoc")
candidate_tag = Tag(name="Candidate", description="Create, Read, Update, Delete Candidates and Predict hiring decision.")

@app.get("/", tags=[home_tag])
def home():
    
    return {"message": "HOME"}

@app.get("/docs", tags=[home_tag])
def docs():
    
    return redirect('/openapi')



@app.get("/candidate", tags=[candidate_tag],
         responses={"200": ListCandidatesSchema, "404": ErrorSchema})
def get_all_candidates():
    """Lista todos os pacientes cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os candidatos")

    session = Session()

    candidates = session.query(Candidate).all()
    
    if not candidates:

        return {"candidates": []}, 200
    else:
        logger.debug(f"%d candidatos econtrados" % len(candidates))
        print(candidates)
        return get_all_candidates(candidates), 200


# @app.post('/paciente', tags=[paciente_tag],
#           responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
# def predict(form: PacienteSchema):
#     """Adiciona um novo paciente à base de dados
#     Retorna uma representação dos pacientes e diagnósticos associados.
    
#     Args:
#         name (str): nome do paciente
#         preg (int): número de vezes que engravidou: Pregnancies
#         plas (int): concentração de glicose no plasma: Glucose
#         pres (int): pressão diastólica (mm Hg): BloodPressure
#         skin (int): espessura da dobra cutânea do tríceps (mm): SkinThickness
#         test (int): insulina sérica de 2 horas (mu U/ml): Insulin
#         mass (float): índice de massa corporal (peso em kg/(altura em m)^2): BMI
#         pedi (float): função pedigree de diabetes: DiabetesPedigreeFunction
#         age (int): idade (anos): Age
        
#     Returns:
#         dict: representação do paciente e diagnóstico associado
#     """
#     # TODO: Instanciar classes

#     # Recuperando os dados do formulário
#     name = form.name
#     preg = form.preg
#     plas = form.plas
#     pres = form.pres
#     skin = form.skin
#     test = form.test
#     mass = form.mass
#     pedi = form.pedi
#     age = form.age
        
#     # Preparando os dados para o modelo
#     X_input = PreProcessador.preparar_form(form)
#     # Carregando modelo
#     model_path = './MachineLearning/pipelines/rf_diabetes_pipeline.pkl'
#     # modelo = Model.carrega_modelo(ml_path)
#     modelo = Pipeline.carrega_pipeline(model_path)
#     # Realizando a predição
#     outcome = int(Model.preditor(modelo, X_input)[0])
    
#     paciente = Paciente(
#         name=name,
#         preg=preg,
#         plas=plas,
#         pres=pres,
#         skin=skin,
#         test=test,
#         mass=mass,
#         pedi=pedi,
#         age=age,
#         outcome=outcome
#     )
#     logger.debug(f"Adicionando produto de nome: '{paciente.name}'")
    
#     try:
#         # Criando conexão com a base
#         session = Session()
        
#         # Checando se paciente já existe na base
#         if session.query(Paciente).filter(Paciente.name == form.name).first():
#             error_msg = "Paciente já existente na base :/"
#             logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
#             return {"message": error_msg}, 409
        
#         # Adicionando paciente
#         session.add(paciente)
#         # Efetivando o comando de adição
#         session.commit()
#         # Concluindo a transação
#         logger.debug(f"Adicionado paciente de nome: '{paciente.name}'")
#         return apresenta_paciente(paciente), 200
    
#     # Caso ocorra algum erro na adição
#     except Exception as e:
#         error_msg = "Não foi possível salvar novo item :/"
#         logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
#         return {"message": error_msg}, 400

    
@app.get("/candidate", tags=[candidate_tag],
         responses={"200": CadidateViewSchema, "404": ErrorSchema})
def get_candidate(query: CandidateIdSchema):
    """
    Args:
       id
        
    Returns:
        
    """

    session = Session()
    candidate_id = unquote(query.id)
    candidate = session.query(Candidate).filter(Candidate.id == candidate_id).first()
    
    if not candidate:
        error_msg = "Candidato não encontrado na base :/"
        logger.warning(f"Erro ao buscar candidato '{candidate_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        print(candidate)
        return get_candidate(candidate), 200


@app.post("/candidate", tags=[candidate_tag],
         responses={"200": CadidateViewSchema, "404": ErrorSchema})
def add_candidate(query: CandidateIdSchema, body: CandidateSchema):
    """
    Args:
       id
        
    Returns:
        
    """

    session = Session()
    candidate_id = unquote(query.id)
    candidate = session.query(Candidate).filter(Candidate.id == candidate_id).first()
    
    if not candidate:
        error_msg = "Candidato não encontrado na base :/"
        logger.warning(f"Erro ao buscar candidato '{candidate_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        candidate.age = body.age
        candidate.gender = body.gender
        candidate.education_level = body.education_level
        candidate.xp_years = body.xp_years
        candidate.prev_cia_worked = body.prev_cia_worked
        candidate.dist_cia = body.dist_cia
        candidate.interview_score = body.interview_score
        candidate.skill_score = body.skill_score
        candidate.personality_score = body.personality_score
        candidate.recruitment_strategy = body.recruitment_strategy
        candidate.hiring_decision = body.hiring_decision
        session.commit()

        logger.debug(f"Candidato '{candidate.id}' atualizado com sucesso")
        return get_candidate(candidate), 200

@app.delete('/candidate', tags=[candidate_tag],
            responses={"200": CadidateViewSchema, "404": ErrorSchema})
def delete_candidate(query: CandidateIdSchema):
    """Remove um paciente cadastrado na base a partir do nome

    Args:
        id (int): candidate id
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    candidate_id = unquote(query.id)
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


if __name__ == '__main__':
    app.run(debug=True)