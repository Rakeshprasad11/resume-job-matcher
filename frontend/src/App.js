import React, { useState } from 'react';

function App() {
  const [resumeData, setResumeData] = useState(null);
  const [error, setError] = useState('');

  const handleParseResume = async () => {
    try {
      const response = await fetch("https://resume-job-matcher-backend.onrender.com/parse_resume");
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
    <div>
      <h1>Resume Parser Tester</h1>
      <button onClick={handleParseResume}>Parse Resume</button>
      {error && <p style={{ color: 'red' }}>❌ {error}</p>}
      {resumeData && (
        <pre>{JSON.stringify(resumeData, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;
