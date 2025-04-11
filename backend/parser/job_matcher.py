import re

def match_skills(resume_skills, job_description):
    # Normalize text
    resume_skills = resume_skills.lower()
    job_description = job_description.lower()

    # Convert resume skills into individual words
    resume_keywords = [skill.strip() for skill in re.split(r'[,\n]', resume_skills) if skill.strip()]

    matched_skills = []
    for skill in resume_keywords:
        # Use word boundaries to ensure clean match (e.g., not matching "sql" inside "sequel")
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, job_description):
            matched_skills.append(skill)

    match_percentage = (len(matched_skills) / len(resume_keywords)) * 100 if resume_keywords else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
