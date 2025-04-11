import re

def clean_skills(text):
    # Remove category headers like "Programming:", "Data & Analytics:", etc.
    lines = text.split('\n')
    all_skills = []
    for line in lines:
        if ':' in line:
            _, skills_str = line.split(':', 1)
        else:
            skills_str = line
        # Remove things like "(Advanced)", "(Basic)"
        skills = re.sub(r'\([^)]*\)', '', skills_str)
        # Split by comma
        all_skills += [skill.strip().lower() for skill in skills.split(',')]
    return set(all_skills)

def match_skills(resume_skills, job_description):
    resume_skills_set = clean_skills(resume_skills)
    job_keywords_set = set(re.findall(r'\b[\w\-\+#.]+\b', job_description.lower()))

    matched_skills = [skill for skill in resume_skills_set if skill in job_keywords_set]
    match_percentage = (len(matched_skills) / len(job_keywords_set)) * 100 if job_keywords_set else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
