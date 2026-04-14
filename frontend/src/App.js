import { useEffect, useState } from "react";

function App() {
  const [msg, setMsg] = useState("");

  useEffect(() => {
    fetch("https://imt-212-project.onrender.com")
      .then((res) => res.json())
      .then((data) => setMsg(data.msg))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h1>Frontend Working 🚀</h1>
      <h2>Backend Response: {msg}</h2>
    </div>
  );
}

export default App;