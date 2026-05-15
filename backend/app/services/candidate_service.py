from app.models.candidate import Candidate
from app.config.database import SessionLocal


def save_candidate(
    filename,
    file_url,
    skills,
    ats_score
):

    db = SessionLocal()

    candidate = Candidate(
        filename=filename,
        file_url=file_url,
        skills=", ".join(skills),
        ats_score=ats_score
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    db.close()

    return candidate