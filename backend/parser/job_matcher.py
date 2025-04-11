import re

def match_skills(resume_skills, job_description):
    resume_skills_list = [s.strip().lower() for s in resume_skills.split(',') if s.strip()]
    matched_skills = []

    for skill in resume_skills_list:
        # Use word boundary to match whole skill words like 'python', 'sql', etc.
        if re.search(r'\b' + re.escape(skill) + r'\b', job_description.lower()):
            matched_skills.append(skill)

    match_percentage = (len(matched_skills) / len(resume_skills_list)) * 100 if resume_skills_list else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
