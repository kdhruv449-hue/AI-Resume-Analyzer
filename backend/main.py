from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from job_analyzer import analyze_job_description
from matcher import calculate_match
from recommendation_engine import generate_recommendations
from semantic_matcher import calculate_semantic_similarity


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://ai-resume-analyzer-frontend-fe4r.onrender.com",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API is running"
    }


@app.post("/analyze")
def analyze():
    return {
        "message": "Resume analysis endpoint is working"
    }


@app.post("/upload-resume")
async def upload_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Check file type
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file."
        )

    # Check job description
    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    temp_file = "temp_resume.pdf"

    try:

        # Read uploaded file
        contents = await resume.read()

        # Save temporary PDF
        with open(temp_file, "wb") as f:
            f.write(contents)

        # Extract resume text
        resume_text = extract_text_from_pdf(temp_file)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume."
            )

        # Extract resume skills
        resume_skills = extract_skills(resume_text)

        # Extract job skills
        job_result = analyze_job_description(job_description)
        job_skills = job_result["skills"]

        # Calculate keyword match
        match_result = calculate_match(
            resume_skills,
            job_skills
        )

        # Generate recommendations
        recommendations = generate_recommendations(
            match_result["missing_skills"]
        )

        # Calculate semantic similarity
        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_description
        )

        # Return final result
        return {
            "filename": resume.filename,
            "resume_skills": resume_skills,
            "job_skills": job_skills,
            "match_score": match_result["score"],
            "matched_skills": match_result["matched_skills"],
            "missing_skills": match_result["missing_skills"],
            "recommendations": recommendations,
            "semantic_similarity": semantic_score
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing resume: {str(e)}"
        )

    finally:

        # Delete temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)