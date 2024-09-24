from pydantic import BaseModel
from typing import List
from model.candidate import Candidate


class CandidateSchema(BaseModel):

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


class CadidateViewSchema(CandidateSchema):

    id: int
    hiring_decision: int


class ListCandidatesSchema(BaseModel):

    candidates: List[CandidateSchema]


class CandidateIdSchema(BaseModel):

    id: int


def format_candidate(candidate: Candidate):
    return {
        "id": candidate.id,
        "email": candidate.email,
        "age": candidate.age,
        "gender": candidate.gender,
        "education_level": candidate.education_level,
        "xp_years": candidate.xp_years,
        "prev_cia_worked": candidate.prev_cia_worked,
        "dist_cia": candidate.dist_cia,
        "interview_score": candidate.interview_score,
        "skill_score": candidate.skill_score,
        "personality_score": candidate.personality_score,
        "recruitment_strategy": candidate.recruitment_strategy,
        "hiring_decision": candidate.hiring_decision,
    }


def format_all_candidates(candidates: List[Candidate]):

    result = []
    for candidate in candidates:
        result.append(
            {
                "id": candidate.id,
                "email": candidate.email,
                "age": candidate.age,
                "gender": candidate.gender,
                "education_level": candidate.education_level,
                "xp_years": candidate.xp_years,
                "prev_cia_worked": candidate.prev_cia_worked,
                "dist_cia": candidate.dist_cia,
                "interview_score": candidate.interview_score,
                "skill_score": candidate.skill_score,
                "personality_score": candidate.personality_score,
                "recruitment_strategy": candidate.recruitment_strategy,
                "hiring_decision": candidate.hiring_decision,
            }
        )

    return {"candidates": result}
