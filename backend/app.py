def extract_skills(text):
    lines = text.split('\n')
    skills = []
    for i, line in enumerate(lines):
        if "SKILLS" in line.upper():
            skills = lines[i+1:i+4]  # change based on your resume
            break
    return '\n'.join(skills)

@app.route('/parse-resume', methods=['GET'])
def parse_resume():
    filename = 'rakesh_resume.pdf'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "Resume not found"}), 404

    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n'

    skills = extract_skills(text)

    return jsonify({
        "resume_text": text,
        "skills": skills
    })
