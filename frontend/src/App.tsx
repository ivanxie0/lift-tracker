import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/health`)
    .then((res) => res.json())
    .then((data) => setStatus (data.status));
  }, []);

  return <h1>Backend status: {status}</h1>;
}

export default App;

