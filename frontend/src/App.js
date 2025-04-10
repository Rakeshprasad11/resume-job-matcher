import React, { useState } from "react";

function App() {
  const [response, setResponse] = useState("");

  const handleClick = async () => {
    try {
      const res = await fetch("http://127.0.0.1:10000/parse-resume");
      const data = await res.json();
      setResponse(JSON.stringify(data, null, 2));
    } catch (err) {
      setResponse("❌ Error fetching resume data");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>📄 Resume Parser Tester</h1>
      <button onClick={handleClick}>Parse Resume</button>
      <pre style={{ background: "#f4f4f4", padding: "1rem" }}>{response}</pre>
    </div>
  );
}

export default App;
