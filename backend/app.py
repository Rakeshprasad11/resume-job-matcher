from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from PyPDF2 import PdfReader

from parser.extract import (
    extract_skills,
    extract_summary,
    extract_education,
    extract_experience,
    extract_projects
)

from parser.job_matcher import match_skills

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return '✅ Flask app is working!'

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

    summary = extract_summary(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience(text)
    projects = extract_projects(text)

    return jsonify({
        "resume_text": text,
        "summary": summary,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects
    })

@app.route('/match-job', methods=['POST'])
def match_job():
    data = request.get_json()

    resume_skills = data.get("resume_skills", "")
    job_description = data.get("job_description", "")

    if not resume_skills or not job_description:
        return jsonify({"error": "Missing skills or job description"}), 400

    result = match_skills(resume_skills, job_description)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
