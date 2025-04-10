def match_skills(resume_skills, job_description):
    resume_skills_set = set(map(str.strip, resume_skills.lower().split(',')))
    job_keywords_set = set(map(str.strip, job_description.lower().split(',')))

    matched_skills = resume_skills_set.intersection(job_keywords_set)
    match_percentage = (len(matched_skills) / len(resume_skills_set)) * 100 if resume_skills_set else 0

    return {
        "matched_skills": list(matched_skills),
        "match_percentage": round(match_percentage, 2)
    }
