from fastapi import FastAPI

from app.routes import resume
from app.routes import job_match

app = FastAPI(
    title="AI Resume Analyzer API",
    description="AI-powered Resume Analyzer and Job Matching Platform",
    version="1.0.0"
)

app.include_router(resume.router)
app.include_router(job_match.router)

@app.get("/")
def home():

    return {
        "message": "AI Resume Analyzer Backend Running Successfully"
    }