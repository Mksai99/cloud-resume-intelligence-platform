from fastapi import APIRouter
from pydantic import BaseModel
from app.services.recommendation import generate_recommendations
from app.services.ats_score import calculate_ats_score

router = APIRouter(
    prefix="/job",
    tags=["Job Matching"]
)


class MatchRequest(BaseModel):

    candidate_skills: list[str]
    required_skills: list[str]


@router.post("/match")

def match_resume(request: MatchRequest):

    result = calculate_ats_score(
        request.candidate_skills,
        request.required_skills
    )

    recommendations = generate_recommendations(
        result["missing_skills"]
    )

    return {
        
        "message": "ATS score calculated successfully",
        "data": result,
        "recommendations": recommendations
        
    }