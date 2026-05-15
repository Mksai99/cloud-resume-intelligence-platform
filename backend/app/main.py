from fastapi import FastAPI
from app.routes import resume

app = FastAPI(
    title="AI Resume Analyzer API",
    description="AI-powered Resume Analyzer and Job Matching Platform",
    version="1.0.0"
)

app.include_router(resume.router)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer Backend Running Successfully"
    }