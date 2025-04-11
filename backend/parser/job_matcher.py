import re

def match_skills(resume_skills, job_description):
    # Step 1: Remove labels like "Programming:", "Cloud:" etc.
    cleaned_resume = re.sub(r'\b\w[\w\s&]+:\s*', '', resume_skills)

    # Step 2: Split skills using comma, normalize case, remove extra whitespace
    resume_skills_list = [s.strip().lower() for s in cleaned_resume.split(',') if s.strip()]

    # Step 3: Extract words from job description for matching
    job_words = re.findall(r'\b[\w\-\+\.#]+\b', job_description.lower())

    # Step 4: Match using intersection
    matched_skills = list(set(resume_skills_list) & set(job_words))
    match_percentage = (len(matched_skills) / len(resume_skills_list)) * 100 if resume_skills_list else 0

    return {
        "matched_skills": matched_skills,
        "match_percentage": round(match_percentage, 2)
    }
