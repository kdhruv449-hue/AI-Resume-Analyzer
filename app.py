import streamlit as st

from resume_parser import extract_text_from_pdf
from text_processor import clean_text
from skill_extractor import extract_skills
from job_analyzer import analyze_job_description
from matcher import calculate_match
from semantic_matcher import calculate_semantic_similarity
from recommendation_engine import generate_recommendations


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI-Powered Resume Analyzer")

st.write(
    "Upload your resume and paste a job description "
    "to analyze your skill match."
)


# Resume upload
uploaded_file = st.file_uploader(
    "Upload your Resume PDF",
    type=["pdf"]
)


# Job description
job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


# Analyze button
if st.button("🔍 Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume PDF.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:

        # Extract resume text
        resume_text = ""

        import pdfplumber

        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    resume_text += text + "\n"


        # Clean resume text
        cleaned_text = clean_text(resume_text)


        # Extract resume skills
        resume_skills = extract_skills(cleaned_text)


        # Analyze job description
        job_result = analyze_job_description(job_description)

        job_skills = job_result["skills"]


        # Calculate keyword match
        match_result = calculate_match(
            resume_skills,
            job_skills
        )


        # Calculate semantic similarity
        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_description
        )


        # Display results
        st.success("Analysis completed successfully! 🎉")


        # Match score
        st.subheader("📊 Match Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Keyword Match Score",
                f"{match_result['score']}%"
            )

        with col2:
            st.metric(
                "Semantic Similarity",
                f"{semantic_score}%"
            )


        # Skills
        st.subheader("🧑‍💻 Resume Skills")

        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.write("No skills detected.")


        st.subheader("💼 Job Required Skills")

        if job_skills:
            st.write(", ".join(job_skills))
        else:
            st.write("No skills detected.")


        # Matched skills
        st.subheader("✅ Matched Skills")

        if match_result["matched_skills"]:
            for skill in match_result["matched_skills"]:
                st.write(f"✓ {skill}")
        else:
            st.write("No matched skills found.")


        # Missing skills
        st.subheader("❌ Missing Skills")

        if match_result["missing_skills"]:
            for skill in match_result["missing_skills"]:
                st.write(f"✗ {skill}")
        else:
            st.write("No missing skills!")


        # Recommendations
        st.subheader("💡 Recommendations")

        recommendations = generate_recommendations(
            match_result["missing_skills"]
        )

        if recommendations:
            for recommendation in recommendations:
                st.write(f"• {recommendation}")
        else:
            st.write("Great job! No additional skills to recommend.")