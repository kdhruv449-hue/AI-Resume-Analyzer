# AI Resume Analyzer

An AI-powered web application that analyzes a resume against a given job description and identifies matching skills, missing skills, semantic similarity, and personalized learning recommendations.

##  Features

- Upload resume in PDF format
- Extract text from resume
- Extract skills from resume
- Analyze job descriptions
- Identify required job skills
- Calculate resume-job match score
- Calculate semantic similarity
- Display matched skills
- Display missing skills
- Generate recommendations for missing skills
- Clean and responsive React frontend

## 🛠️ Tech Stack

### Frontend
- React.js
- JavaScript
- HTML
- CSS
- Vite

### Backend
- Python
- FastAPI
- PDF text extraction
- NLP / semantic similarity

### Tools
- Git
- GitHub
- VS Code

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── backend/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── job_analyzer.py
├── matcher.py
├── semantic_matcher.py
├── recommendation_engine.py
├── skill_database.py
├── text_processor.py
├── requirements.txt
├── .gitignore
└── README.md