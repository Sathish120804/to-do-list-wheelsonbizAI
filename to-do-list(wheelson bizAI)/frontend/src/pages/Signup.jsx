import { useState } from "react";
import axios from "axios";
import "../App.css";

function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {
    try {
      if (!email || !password) {
        alert("Please enter all fields");
        return;
      }

      await axios.post(
        "http://localhost:5000/api/auth/signup",
        {
          email,
          password,
        }
      );

      alert("Signup Successful");
      window.location = "/";
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
        Already have an account?
        <a href="/"> Sign In</a>
      </p>
    </div>
  );
}

export default Signup;