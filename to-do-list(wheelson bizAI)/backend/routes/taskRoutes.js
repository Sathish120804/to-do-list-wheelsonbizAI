const express = require("express");
const jwt = require("jsonwebtoken");
const pool = require("../db");

const router = express.Router();

// Middleware
const auth = (req, res, next) => {
  const token = req.headers.authorization;

  if (!token) {
    return res.status(401).json({
      message: "Token Missing",
    });
  }

  try {
    const decoded = jwt.verify(
      token,
      process.env.JWT_SECRET
    );

    req.user = decoded;

    next();
  } catch (error) {
    res.status(401).json({
      message: "Invalid Token",
    });
  }
};

// GET ALL TASKS
router.get("/", auth, async (req, res) => {
  try {
    const result = await pool.query(
      "SELECT * FROM tasks WHERE user_id=$1 ORDER BY id DESC",
      [req.user.id]
    );

    res.json(result.rows);
  } catch (error) {
    console.log(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

// ADD TASK
router.post("/", auth, async (req, res) => {
  try {
    const { title } = req.body;

    const result = await pool.query(
      "INSERT INTO tasks(title,user_id) VALUES($1,$2) RETURNING *",
      [title, req.user.id]
    );

    res.status(201).json(result.rows[0]);
  } catch (error) {
    console.log(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

// COMPLETE TASK
router.put("/:id", auth, async (req, res) => {
  try {
    await pool.query(
      "UPDATE tasks SET completed=true WHERE id=$1",
      [req.params.id]
    );

    res.json({
      message: "Task Completed",
    });
  } catch (error) {
    console.log(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

// DELETE TASK
router.delete("/:id", auth, async (req, res) => {
  try {
    await pool.query(
      "DELETE FROM tasks WHERE id=$1",
      [req.params.id]
    );

    res.json({
      message: "Task Deleted",
    });
  } catch (error) {
    console.log(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

module.exports = router;