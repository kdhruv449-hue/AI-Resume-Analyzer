import { useState } from "react";
import "./index.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleAnalyze = async () => {
    if (!resume) {
      setMessage("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setMessage("Please enter a job description.");
      return;
    }

    setLoading(true);
    setMessage("");
    setResult(null);

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch("https://ai-resume-analyzer-p93l.onrender.com/upload-resume", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      setResult(data);
      setMessage("Resume analyzed successfully!");
    } catch (error) {
      console.error(error);
      setMessage(error.message || "Failed to fetch");
    } finally {
      setLoading(false);
    }
  };

  const getScoreClass = (score) => {
    if (score >= 70) return "score-high";
    if (score >= 40) return "score-medium";
    return "score-low";
  };

  return (
    <div className="app">
      <div className="container">

        {/* Header */}
        <header className="header">
          <h1>AI Resume Analyzer</h1>
          <p>
            Analyze your resume against any job description using AI.
          </p>
        </header>

        {/* Upload Resume */}
        <div className="form-section">
          <label htmlFor="resume">
            Upload Resume PDF
          </label>

          <div className="file-box">
            <input
              id="resume"
              type="file"
              accept=".pdf"
              onChange={(e) => {
                setResume(e.target.files[0]);
                setMessage("");
              }}
            />

            {resume && (
              <span className="file-name">
                {resume.name}
              </span>
            )}
          </div>
        </div>

        {/* Job Description */}
        <div className="form-section">
          <label htmlFor="jobDescription">
            Job Description
          </label>

          <textarea
            id="jobDescription"
            value={jobDescription}
            onChange={(e) => {
              setJobDescription(e.target.value);
              setMessage("");
            }}
            placeholder="Paste job description here..."
            rows="10"
          />
        </div>

        {/* Analyze Button */}
        <button
          className="analyze-btn"
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading ? "Analyzing Resume..." : "Analyze Resume"}
        </button>

        {/* Message */}
        {message && (
          <div
            className={
              message.toLowerCase().includes("success")
                ? "success-message"
                : "error-message"
            }
          >
            {message}
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="results">

            <div className="result-header">
              <h2>Analysis Results</h2>
              <p>Your resume analysis is complete.</p>
            </div>

            {/* Scores */}
            <div className="scores">

              {/* Match Score */}
              <div className="score-box">
                <p className="score-title">Match Score</p>

                <div
  className="score-circle"
  style={{
    background: `conic-gradient(
      #22c55e ${result.match_score}%,
      #e5e7eb ${result.match_score}% 100%
    )`,
  }}
>
  <div className="score-inner">
    <span>{result.match_score}%</span>
  </div>
</div>
              </div>

              {/* Semantic Similarity */}
              <div className="score-box">
                <p className="score-title">
                  Semantic Similarity
                </p>

<div
  className="score-circle"
  style={{
    background: `conic-gradient(
      #3b82f6 ${result.semantic_similarity}%,
      #e5e7eb ${result.semantic_similarity}% 100%
    )`,
  }}
>
  <div className="score-inner">
    <span>
      {result.semantic_similarity}%
    </span>
  </div>
</div>
              </div>

            </div>

            {/* Resume Skills */}
            <div className="skill-section">
              <h3>Resume Skills</h3>

              <div className="skill-list">
                {result.resume_skills &&
                  result.resume_skills.map((skill, index) => (
                    <span
                      className="skill-badge"
                      key={index}
                    >
                      {skill}
                    </span>
                  ))}
              </div>
            </div>

            {/* Job Skills */}
            <div className="skill-section">
              <h3>Job Skills</h3>

              <div className="skill-list">
                {result.job_skills &&
                  result.job_skills.map((skill, index) => (
                    <span
                      className="skill-badge"
                      key={index}
                    >
                      {skill}
                    </span>
                  ))}
              </div>
            </div>

            {/* Matched Skills */}
            <div className="skill-section matched-section">
              <h3>Matched Skills</h3>

              <div className="skill-list">
                {result.matched_skills &&
                result.matched_skills.length > 0 ? (
                  result.matched_skills.map((skill, index) => (
                    <span
                      className="matched-badge"
                      key={index}
                    >
                      {skill}
                    </span>
                  ))
                ) : (
                  <p className="empty-text">
                    No matching skills found.
                  </p>
                )}
              </div>
            </div>

            {/* Missing Skills */}
            <div className="skill-section missing-section">
              <h3>Missing Skills</h3>

              <div className="skill-list">
                {result.missing_skills &&
                result.missing_skills.length > 0 ? (
                  result.missing_skills.map((skill, index) => (
                    <span
                      className="missing-badge"
                      key={index}
                    >
                      {skill}
                    </span>
                  ))
                ) : (
                  <p className="success-text">
                    Excellent! No major missing skills.
                  </p>
                )}
              </div>
            </div>

            {/* Recommendations */}
            <div className="recommendations">
              <h3>Recommendations</h3>

              {result.recommendations &&
              result.recommendations.length > 0 ? (
                <ul>
                  {result.recommendations.map(
                    (recommendation, index) => (
                      <li key={index}>
                        {recommendation}
                      </li>
                    )
                  )}
                </ul>
              ) : (
                <p>
                  No additional recommendations available.
                </p>
              )}
            </div>

            {/* Download */}
            <button
              className="download-btn"
              onClick={() => window.print()}
            >
              Download Analysis
            </button>

          </div>
        )}
      </div>
    </div>
  );
}

export default App;