from pydantic import BaseModel
from typing import Optional, List
from model.candidate import Candidate
import json
import numpy as np

class CandidateSchema(BaseModel):

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
    hiring_decision: int 

    
class CadidateViewSchema(CandidateSchema):

    id: int

    
# class PacienteBuscaSchema(BaseModel):
#     """Define como deve ser a estrutura que representa a busca.
#     Ela será feita com base no nome do paciente.
#     """
#     name: str = "Maria"

class ListCandidatesSchema(BaseModel):

    candidates: List[CandidateSchema]

    
class CandidateIdSchema(BaseModel):

    id: int
    

def get_candidate(candidate: Candidate):

    return {
        "id": candidate.id,
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
        "hiring_decision": candidate.hiring_decision
    }
    

def get_all_candidates(candidates: List[Candidate]):

    result = []
    for candidate in candidates:
        result.append({
            "id": candidate.id,
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
            "hiring_decision": candidate.hiring_decision
        })

    return {"candidates": result}