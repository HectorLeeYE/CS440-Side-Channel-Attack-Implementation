import Swal from 'sweetalert2'
import './App.css'
import { useNavigate } from 'react-router-dom'


function App() {
  const navigate = useNavigate();
  const handleLogin = async () => {
    Swal.fire({
      title: "🤓 Login 🤓",
      html: `
        <input id="swal-input1" class="swal2-input" type="password" placeholder="Password">
      `,
      focusConfirm: false,
      preConfirm: () => {
        return [
          document.getElementById("swal-input1").value,
        ]
      }
    }).then(async ({ value, isConfirmed }) => {
      if (isConfirmed) {
        const payload = {
          "password": value
        }
        try {
          //We're posting to the flask
          const response = fetch("http://127.0.0.1:5000/timingAttack", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
          });

          const data = await response;

          if (data.status === 200) {
            Swal.fire({ 
              icon: "success", 
              title: "Success",
              text: "Correct, you've cracked the password! Redirecting..."
            });
            navigate("/landing")
          } else {
            Swal.fire({
              icon: "error",
              title: "Wrong",
              text: "Lol Wrong Password 👎👎",
            });
          }
        }
        catch (error) {
          console.error("Login Failed: ", error)
          Swal.fire({
            icon: "error",
            title: "Wrong",
            text: "If you see this that means you tried something funny like intercepting the request. This is just a demo, so please stop it. Get some help.",
          });
        }
      }
    })
  }

  return (
    <div>
      <h1>CS440 Project</h1>
      <p>Group Number: (TODO: insert group number here)</p>
      <button onClick={handleLogin}>Login</button>
    </div>
  )
}

export default App
