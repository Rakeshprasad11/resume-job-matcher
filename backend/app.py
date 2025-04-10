from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 Important to allow frontend to access backend

@app.route('/')
def home():
    return '✅ Flask app is working!'

@app.route('/parse-resume', methods=['GET'])
def parse_resume():
    resume_text = """
RAKESH PRASAD B R
7899224260 | rakeshprasadbr11@gmail.com
LinkedIn: www.linkedin.com/in/rakesh-prasad-b-r-4a2942243 |
GitHub: github.com/Rakeshprasad11

SUMMARY :-
Computer Science graduate with experience in data analytics and software development.
Proven track record of improving data processing efficiency by 30% and developing machine
learning models with 85% accuracy. Seeking a Data Analyst or Junior Developer position.
...
"""
    return jsonify({"resume_text": resume_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
