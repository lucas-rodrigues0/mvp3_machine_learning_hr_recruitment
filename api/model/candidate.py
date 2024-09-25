from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from typing import Union

from model import Base


class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column("Email", String, unique=True)
    age = Column("Age", Integer)
    gender = Column("Gender", Integer)
    education_level = Column("EducationLevel", Integer)
    xp_years = Column("ExperienceYears", Integer)
    prev_cia_worked = Column("PreviousCompanyWorked", Integer)
    dist_cia = Column("DistanceFromCompany", Float)
    interview_score = Column("InterviewScore", Integer)
    skill_score = Column("SkillScore", Integer)
    personality_score = Column("PersonalityScore", Integer)
    recruitment_strategy = Column("RecruitmentStrategy", Integer)
    hiring_decision = Column("HiringDecision", Integer)
    created_at = Column("CreatedAt", DateTime, default=datetime.now())
    updated_at = Column("UpdatedAt", DateTime, default=datetime.now())

    def __init__(
        self,
        email: str,
        age: int,
        gender: int,
        education_level: int,
        xp_years: int,
        prev_cia_worked: int,
        dist_cia: float,
        interview_score: int,
        skill_score: int,
        personality_score: int,
        recruitment_strategy: int,
        hiring_decision: int,
        created_at: Union[DateTime, None] = None,
        updated_at: Union[DateTime, None] = None,
    ):
        self.email = email
        self.age = age
        self.gender = gender
        self.education_level = education_level
        self.xp_years = xp_years
        self.prev_cia_worked = prev_cia_worked
        self.dist_cia = dist_cia
        self.interview_score = interview_score
        self.skill_score = skill_score
        self.personality_score = personality_score
        self.recruitment_strategy = recruitment_strategy
        self.hiring_decision = hiring_decision

        if created_at:
            print(created_at, "CREATED AT")
            self.created_at = created_at

        if updated_at:
            print(updated_at, "UPDATED AT")
            self.updated_at = updated_at
