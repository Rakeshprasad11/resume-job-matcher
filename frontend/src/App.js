import React, { useState } from 'react';

function App() {
  const [resumeData, setResumeData] = useState(null);
  const [error, setError] = useState('');

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
        </div>
      )}
    </div>
  );
}

export default App;
