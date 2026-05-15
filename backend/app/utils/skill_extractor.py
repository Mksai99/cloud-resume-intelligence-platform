TECH_SKILLS = [
    "python",
    "java",
    "c++",
    "aws",
    "docker",
    "kubernetes",
    "sql",
    "mysql",
    "postgresql",
    "javascript",
    "react",
    "nodejs",
    "fastapi",
    "flask",
    "django",
    "git",
    "linux",
    "terraform",
    "jenkins",
    "html",
    "css",
    "mongodb",
    "machine learning",
    "data analytics",
    "power bi"
]


def extract_skills(cleaned_text):

    detected_skills = []

    for skill in TECH_SKILLS:

        if skill.lower() in cleaned_text:
            detected_skills.append(skill)

    return list(set(detected_skills))