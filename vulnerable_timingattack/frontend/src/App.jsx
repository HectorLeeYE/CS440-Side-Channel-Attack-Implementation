import Swal from 'sweetalert2';
import './App.css';
import { useNavigate } from 'react-router-dom';
import angryCat from '../static/angry-cat-stare.gif'

function App() {
  const navigate = useNavigate();

  const handleLogin = async () => {
    const { value: password, isConfirmed } = await Swal.fire({
      title: "🤓 Login 🤓",
      html: `
        <input id="swal-input1" class="swal2-input" type="password" placeholder="Password">
      `,
      focusConfirm: false,
      confirmButtonColor: "#98fb98",

      preConfirm: () => {
        const el = document.getElementById("swal-input1");
        return el ? el.value : "";
      }
    });

    if (!isConfirmed) return;

    if (!password || typeof password !== "string") {
      await Swal.fire({
        icon: "warning",
        title: "Missing password",
        text: "Please enter your password."
      });
      return;
    }

    const payload = { password };

    try {
      const response = await fetch("http://127.0.0.1:5000/timingAttack", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const body = await response.json().catch(() => null);

      if (response.ok) {
        await Swal.fire({
          icon: "success",
          title: "Success",
          text: "Correct, you've cracked the password! Redirecting..."
        });
        navigate("/landing");
      } else {
        await Swal.fire({
          icon: "error",
          title: "Wrong",
          text: body?.Message || "Lol Wrong Password 👎👎",
        });
      }
    } catch (error) {
      await Swal.fire({
        icon: "error",
        title: "Network/Error",
        text: "Something went wrong sending the request.",
      });
    }
  };

  return (
    <div>
      <h1>CS440 Project</h1>
      <p>Group Number: 9</p>
      <button onClick={handleLogin} style={{ backgroundColor: "#98fb98", border: "none", padding: "8px 16px", borderRadius: "6px" }}>
        Login
      </button>
      <br></br>
      <img src={angryCat} alt="Angry Cat" />
    </div>
  );
}

export default App;
