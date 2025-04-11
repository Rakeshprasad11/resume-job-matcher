import re

def match_skills(resume_skills, job_description):
    resume_skills_set = set(map(str.strip, resume_skills.lower().split(',')))
    job_text = job_description.lower()

    matched_skills = []
    for skill in resume_skills_set:
        # Check if the skill is a standalone word or phrase in the job description
        if skill and re.search(rf'\b{re.escape(skill)}\b', job_text):
            matched_skills.append(skill)

    match_percentage = (len(matched_skills) / len(resume_skills_set)) * 100 if resume_skills_set else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
