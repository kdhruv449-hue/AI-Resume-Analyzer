RECOMMENDATIONS = {
    "python": "Practice Python programming and build real-world projects.",
    "sql": "Practice SQL queries, joins, subqueries and database design.",
    "machine learning": "Learn supervised and unsupervised learning and build ML projects.",
    "deep learning": "Learn neural networks and frameworks such as PyTorch or TensorFlow.",
    "fastapi": "Learn REST API development using FastAPI and build a backend project.",
    "docker": "Learn Docker basics, images, containers and Docker Compose.",
    "aws": "Learn AWS fundamentals such as EC2, S3, IAM and deployment.",
    "react": "Learn React components, props, state and API integration.",
    "javascript": "Strengthen JavaScript fundamentals and modern ES6+ features.",
    "java": "Practice Java OOP, collections and backend development.",
    "c++": "Practice C++ data structures, algorithms and object-oriented programming.",
    "git": "Practice Git commands, branching, merging and collaborative workflows.",
    "github": "Learn GitHub workflows, pull requests and project collaboration.",
    "linux": "Practice Linux commands, file management and shell basics.",
    "pandas": "Practice data manipulation and analysis using Pandas.",
    "numpy": "Practice numerical computing and array operations using NumPy.",
    "opencv": "Build computer vision projects using OpenCV."
}


def generate_recommendations(missing_skills):
    recommendations = []

    for skill in missing_skills:
        if skill in RECOMMENDATIONS:
            recommendations.append(
                f"{skill}: {RECOMMENDATIONS[skill]}"
            )
        else:
            recommendations.append(
                f"{skill}: Consider learning and practicing this skill."
            )

    return recommendations