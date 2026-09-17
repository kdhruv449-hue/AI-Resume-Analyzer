# 📄 AI Resume Analyzer

An AI-powered web application that analyzes a resume against a job description and identifies matching skills, missing skills, recommendations, and similarity scores.

## 🚀 Live Demo

👉 https://ai-resume-analyzer-frontend-fe4r.onrender.com

## ✨ Features

- 📄 Upload resume in PDF format
- 🔍 Extract technical skills from resumes
- 📝 Analyze job descriptions
- 📊 Calculate resume–job match score
- 🧠 Calculate text similarity
- ✅ Show matched skills
- ❌ Identify missing skills
- 💡 Generate learning recommendations
- 🌐 React frontend
- ⚡ FastAPI backend
- 📱 Responsive web interface
- 🔗 Deployed frontend and backend

## 🖥️ Screenshots

### Home Page

Add your screenshot here:

![Home Page](screenshots/home.png)

### Analysis Results

Add your results screenshot here:

![Analysis Results](screenshots/results.png)

## 🛠️ Tech Stack

### Frontend
- React
- JavaScript
- CSS
- Vite

### Backend
- Python
- FastAPI
- Uvicorn
- pdfplumber

### NLP / Matching
- Python text processing
- Regex-based skill extraction
- Keyword matching
- Cosine similarity

### Deployment
- GitHub
- Render

## 🏗️ Project Architecture

```text
User
  │
  ▼
React Frontend
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  ├── Resume PDF Extraction
  │
  ├── Skill Extraction
  │
  ├── Job Description Analysis
  │
  ├── Keyword Matching
  │
  ├── Similarity Calculation
  │
  └── Recommendation Engine
  │
  ▼
Analysis Results
  │
  ▼
React UI