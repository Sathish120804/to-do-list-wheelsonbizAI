import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import "../App.css";

function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSignup = async () => {
    try {
      if (!email || !password) {
        alert("Please enter all fields");
        return;
      }

      await axios.post(
        "https://to-do-list-wheelsonbizai.onrender.com/api/auth/signup",
        {
          email,
          password,
        }
      );

      alert("Signup Successful");

      navigate("/");
    } catch (error) {
      alert("Email already exists");
    }
  };

  return (
    <div className="container">
      <h2>Create Account</h2>

      <input
        type="email"
        placeholder="Enter Email"
        value={email}
        onChange={(e) =>
          setEmail(e.target.value)
        }
      />

      <input
        type="password"
        placeholder="Enter Password"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <button onClick={handleSignup}>
        Sign Up
      </button>

      <p className="link-text">
        Already have an account?{" "}
        <Link to="/">
          Sign In
        </Link>
      </p>
    </div>
  );
}

export default Signup;