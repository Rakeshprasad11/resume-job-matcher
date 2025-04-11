import re

def match_skills(resume_skills, job_description):
    resume_skills_list = [skill.strip().lower() for skill in resume_skills.split(',')]
    job_description_lower = job_description.lower()

    matched_skills = []
    for skill in resume_skills_list:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, job_description_lower):
            matched_skills.append(skill)

    match_percentage = (len(matched_skills) / len(resume_skills_list)) * 100 if resume_skills_list else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
