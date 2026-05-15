def calculate_ats_score(candidate_skills, required_skills):

    candidate_skills = set(
        skill.lower()
        for skill in candidate_skills
    )

    required_skills = set(
        skill.lower()
        for skill in required_skills
    )

    matched_skills = candidate_skills.intersection(
        required_skills
    )

    missing_skills = required_skills.difference(
        candidate_skills
    )

    ats_score = (
        len(matched_skills) / len(required_skills)
    ) * 100 if required_skills else 0

    return {
        "ats_score": round(ats_score, 2),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }