def extract_skills(text):
    lines = text.split('\n')
    skills = []
    for i, line in enumerate(lines):
        if "SKILLS" in line.upper():
            skills = lines[i+1:i+4]
            break
    return '\n'.join(skills)

def extract_summary(text):
    lines = text.split('\n')
    summary = []
    for i, line in enumerate(lines):
        if "SUMMARY" in line.upper():
            summary = lines[i+1:i+4]
            break
    return '\n'.join(summary)
