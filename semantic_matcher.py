from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, job_description):

    resume_embedding = model.encode(resume_text)
    job_embedding = model.encode(job_description)

    similarity = np.dot(resume_embedding, job_embedding) / (
        np.linalg.norm(resume_embedding)
        * np.linalg.norm(job_embedding)
    )

    score = float(similarity * 100)

    return round(score, 2)
