import { useEffect, useState } from "react";
import axios from "axios";
import "../App.css";

function Dashboard() {
  const [title, setTitle] = useState("");
  const [tasks, setTasks] = useState([]);

  const token =
    localStorage.getItem("token");

  const loadTasks = async () => {
    try {
      const res = await axios.get(
        "http://localhost:5000/api/tasks",
        {
          headers: {
            authorization: token,
          },
        }
      );

      setTasks(res.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const addTask = async () => {
    if (!title) {
      alert("Enter task");
      return;
    }

    try {
      await axios.post(
        "https://to-do-list-wheelsonbizai.onrender.com/api/tasks",
        {
          title,
        },
        {
          headers: {
            authorization: token,
          },
        }
      );

      setTitle("");

      loadTasks();
    } catch (error) {
      console.log(error);
    }
  };

  const completeTask = async (id) => {
    try {
      await axios.put(
        `http://localhost:5000/api/tasks/${id}`,
        {},
        {
          headers: {
            authorization: token,
          },
        }
      );

      loadTasks();
    } catch (error) {
      console.log(error);
    }
  };

  const deleteTask = async (id) => {
    try {
      await axios.delete(
        `http://localhost:5000/api/tasks/${id}`,
        {
          headers: {
            authorization: token,
          },
        }
      );

      loadTasks();
    } catch (error) {
      console.log(error);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    window.location = "/";
  };

  return (
    <div className="container dashboard">

      <div className="header">
        <h2>Todo Dashboard</h2>

        <button
          className="logout-btn"
          onClick={logout}
        >
          Logout
        </button>
      </div>

      <h3>
        Total Tasks: {tasks.length}
      </h3>

      <div className="task-input">
        <input
          type="text"
          placeholder="Enter New Task"
          value={title}
          onChange={(e) =>
            setTitle(e.target.value)
          }
        />

        <button onClick={addTask}>
          Add Task
        </button>
      </div>

      {tasks.map((task) => (
        <div
          className="task-card"
          key={task.id}
        >
          <span
            className={
              task.completed
                ? "completed"
                : ""
            }
          >
            {task.title}
          </span>

          <div className="action-buttons">

            {!task.completed && (
              <button
                onClick={() =>
                  completeTask(task.id)
                }
              >
                Complete
              </button>
            )}

            <button
              className="delete-btn"
              onClick={() =>
                deleteTask(task.id)
              }
            >
              Delete
            </button>

          </div>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;