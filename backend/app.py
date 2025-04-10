from flask import Flask, jsonify
import os
from PyPDF2 import PdfReader

app = Flask(__name__)

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

    return jsonify({"resume_text": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
