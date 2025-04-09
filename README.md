# 💼 AI-Powered Resume Parser + Job Matcher

This project is a full-stack AI-powered app that allows users to paste their resume and get instant job recommendations based on their skills using GPT and real-time job listings.

## 🌐 Live Demo
> (Add Vercel + Render links after deployment)

## ⚙️ Tech Stack

| Frontend | Backend | AI & NLP | Data |
|----------|---------|----------|------|
| React    | Flask   | OpenAI GPT-4o | SerpAPI |
| CSS      | Python  | Resume Skill Extraction | Job Matching |

---

## 🔥 Features

- 📄 Resume skill extraction using GPT
- 🔍 Real-time job scraping from Google Jobs (SerpAPI)
- 🎯 Matches jobs based on extracted technical skills
- ⚙️ Backend served via Flask
- 💻 Modern UI using React

---

## 🛠️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Rakeshprasad11/resume-job-matcher.git
cd resume-job-matcher
```

### 2. Setup backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
python app.py
```

> Add your `OPENAI_API_KEY` and `SERPAPI_KEY` in a `.env` file.

### 3. Setup frontend
```bash
cd frontend
npm install
npm start
```

---

## 📦 Environment Variables

Create a `.env` file in the `backend/` folder with:

```env
OPENAI_API_KEY=your_openai_api_key
SERPAPI_KEY=your_serpapi_key
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)