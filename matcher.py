def calculate_match(resume_skills, job_skills):

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set & job_set

    missing_skills = job_set - resume_set

    if len(job_set) == 0:
        score = 0
    else:
        score = (len(matched_skills) / len(job_set)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }