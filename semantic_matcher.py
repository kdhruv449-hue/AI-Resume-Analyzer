import math
import re
from collections import Counter


def tokenize(text):
    return re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())


def calculate_semantic_similarity(resume_text, job_description):
    resume_words = tokenize(resume_text)
    job_words = tokenize(job_description)

    if not resume_words or not job_words:
        return 0.0

    resume_count = Counter(resume_words)
    job_count = Counter(job_words)

    all_words = set(resume_count) | set(job_count)

    resume_vector = [resume_count[word] for word in all_words]
    job_vector = [job_count[word] for word in all_words]

    dot_product = sum(
        a * b for a, b in zip(resume_vector, job_vector)
    )

    resume_magnitude = math.sqrt(
        sum(a * a for a in resume_vector)
    )

    job_magnitude = math.sqrt(
        sum(b * b for b in job_vector)
    )

    if resume_magnitude == 0 or job_magnitude == 0:
        return 0.0

    similarity = dot_product / (
        resume_magnitude * job_magnitude
    )

    score = similarity * 100

    return round(score, 2)