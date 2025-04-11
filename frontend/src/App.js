import React, { useState } from 'react';

function App() {
  const [resumeData, setResumeData] = useState(null);
  const [error, setError] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [matchResult, setMatchResult] = useState(null);

  const handleParseResume = async () => {
    try {
      const response = await fetch("https://resume-job-matcher-backend.onrender.com/parse-resume");
      const data = await response.json();

      if (data.error) {
        setError(data.error);
        setResumeData(null);
      } else {
        setResumeData(data);
        setError('');
      }
    } catch (err) {
      setError("Error fetching resume data");
      setResumeData(null);
    }
  };

  const handleMatchJob = async () => {
    try {
      const response = await fetch("https://resume-job-matcher-backend.onrender.com/match-job", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          resume_skills: resumeData?.skills || "",
          job_description: jobDescription,
        }),
      });

      const data = await response.json();
      setMatchResult(data);
    } catch (err) {
      console.error("Matching failed", err);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>📄 Resume Parser Tester</h1>
      <button onClick={handleParseResume}>🔍 Parse Resume</button>

      {error && <p style={{ color: 'red' }}>❌ {error}</p>}

      {resumeData && (
        <div>
          <h3>✅ Extracted Resume Text</h3>
          <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#f4f4f4", padding: "10px" }}>
            {resumeData.resume_text}
          </pre>

          {resumeData.summary && (
            <div>
              <h3>📝 Summary Extracted</h3>
              <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#fff3e0", padding: "10px" }}>
                {resumeData.summary}
              </pre>
            </div>
          )}

          {resumeData.skills && (
            <div>
              <h3>🛠️ Skills Extracted</h3>
              <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#e8f5e9", padding: "10px" }}>
                {resumeData.skills}
              </pre>
            </div>
          )}

          {resumeData.education && (
            <div>
              <h3>🎓 Education</h3>
              <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#e3f2fd", padding: "10px" }}>
                {resumeData.education}
              </pre>
            </div>
          )}

          {resumeData.experience && (
            <div>
              <h3>🧪 Experience</h3>
              <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#fce4ec", padding: "10px" }}>
                {resumeData.experience}
              </pre>
            </div>
          )}

          {resumeData.projects && (
            <div>
              <h3>💡 Projects</h3>
              <pre style={{ textAlign: 'left', whiteSpace: 'pre-wrap', background: "#ede7f6", padding: "10px" }}>
                {resumeData.projects}
              </pre>
            </div>
          )}

          <div style={{ marginTop: "30px" }}>
            <h2>🧪 Match Resume to Job</h2>
            <textarea
              rows="6"
              cols="60"
              placeholder="Paste job description here..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              style={{ padding: "10px", fontFamily: "Arial" }}
            />
            <br />
            <button onClick={handleMatchJob} style={{ marginTop: "10px" }}>
              🎯 Match Resume with Job
            </button>
          </div>

          {matchResult && (
            <div style={{ marginTop: "20px", background: "#e3f2fd", padding: "15px", borderRadius: "10px" }}>
              <h3>📊 Match Result</h3>
              <p>
                <strong>Match Percentage:</strong>{' '}
                <span style={{
                  color:
                    matchResult.match_percentage >= 70 ? 'green' :
                    matchResult.match_percentage >= 40 ? 'orange' : 'red',
                  fontWeight: "bold"
                }}>
                  {matchResult.match_percentage}%
                </span>
              </p>
              <p>
                <strong>Matched Skills:</strong>{' '}
                <span style={{ color: "#2e7d32" }}>
                  {matchResult.matched_skills.length > 0
                    ? matchResult.matched_skills.join(', ')
                    : 'None'}
                </span>
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
