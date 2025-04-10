from parser.extract import extract_skills, extract_summary
from flask import Flask, jsonify
from flask_cors import CORS
import os
from PyPDF2 import PdfReader

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return '✅ Flask app is working!'

def extract_skills(text):
    lines = text.split('\n')
    skills = []
    for i, line in enumerate(lines):
        if "SKILLS" in line.upper():
            skills = lines[i+1:i+4]  # You can tweak the range
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
    summary = extract_summary(text)

    return jsonify({
        "resume_text": text,
        "skills": skills,
        "summary": summary
    })

