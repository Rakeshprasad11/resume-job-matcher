def extract_section(text, start_keywords, stop_keywords):
    lines = text.split('\n')
    section = []
    capture = False
    for line in lines:
        if any(kw in line.upper() for kw in start_keywords):
            capture = True
            continue
        if capture and any(kw in line.upper() for kw in stop_keywords):
            break
        if capture:
            section.append(line)
    return '\n'.join(section).strip()


def extract_summary(text):
    return extract_section(
        text,
        start_keywords=["SUMMARY"],
        stop_keywords=["EDUCATION", "EXPERIENCE", "PROJECTS", "SKILLS", "INTERNSHIP"]
    )


def extract_education(text):
    return extract_section(
        text,
        start_keywords=["EDUCATION"],
        stop_keywords=["EXPERIENCE", "PROJECTS", "SKILLS", "SUMMARY"]
    )


def extract_experience(text):
    return extract_section(
        text,
        start_keywords=["EXPERIENCE", "INTERNSHIP EXPERIENCE"],
        stop_keywords=["PROJECTS", "SKILLS", "EDUCATION", "SUMMARY"]
    )


def extract_skills(text):
    return extract_section(
        text,
        start_keywords=["SKILLS"],
        stop_keywords=["EDUCATION", "PROJECTS", "SUMMARY", "EXPERIENCE"]
    )


def extract_projects(text):
    return extract_section(
        text,
        start_keywords=["PROJECTS", "PROJECTS & LEADERSHIP"],
        stop_keywords=["SKILLS", "EXPERIENCE", "EDUCATION", "SUMMARY"]
    )
