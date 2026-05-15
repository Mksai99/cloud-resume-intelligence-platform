from app.config.database import engine
from app.models.candidate import Candidate
from app.config.database import Base

Base.metadata.create_all(bind=engine)

print("Database tables created successfully")