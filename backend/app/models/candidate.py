from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base

class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    file_url = Column(String)

    skills = Column(String)

    ats_score = Column(Float)