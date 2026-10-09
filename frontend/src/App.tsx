import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
    .then((res) => res.json())
    .then((data) => setStatus (data.status));
  }, []);

  return <h1>Backend status: {status}</h1>;
}

export default App;

