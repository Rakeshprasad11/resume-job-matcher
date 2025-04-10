def extract_skills(text):
    lines = text.split('\n')
    skills = []
    for i, line in enumerate(lines):
        if "SKILLS" in line.upper():
            skills = lines[i+1:i+4]
            break
    return '\n'.join(skills)


def extract_education(text):
    lines = text.split('\n')
    education = []
    for i, line in enumerate(lines):
        if "EDUCATION" in line.upper():
            education = lines[i+1:i+5]
            break
    return '\n'.join(education)


def extract_summary(text):
    lines = text.split('\n')
    summary = []
    for i, line in enumerate(lines):
        if "SUMMARY" in line.upper():
            summary = lines[i+1:i+4]
            break
    return '\n'.join(summary)

def extract_experience(text):
    lines = text.split('\n')
    experience = []
    for i, line in enumerate(lines):
        if "INTERNSHIP EXPERIENCE" in line.upper() or "EXPERIENCE" in line.upper():
            experience = lines[i+1:i+6]  # Adjust as needed
            break
    return '\n'.join(experience)

def extract_projects(text):
    lines = text.split('\n')
    projects = []
    for i, line in enumerate(lines):
        if "PROJECTS" in line.upper():
            projects = lines[i+1:i+6]  # Adjust based on your resume
            break
    return '\n'.join(projects)
