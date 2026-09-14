from skill_extractor import extract_skills


def analyze_job_description(job_description):

    skills = extract_skills(job_description)

    return {
        "skills": skills
    }

if __name__ == "__main__":

    job_description = """
    We are looking for a Python developer with
    SQL, FastAPI and Docker experience.
    Knowledge of AWS and Machine Learning is preferred.
    """

    result = analyze_job_description(job_description)

    print("========== JOB SKILLS ==========")

    for skill in result["skills"]:
        print("✓", skill)