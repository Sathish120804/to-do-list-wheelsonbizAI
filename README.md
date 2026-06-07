# Todo List Web Application

A full-stack Todo List Web Application developed using React, Node.js, Express.js, PostgreSQL (Neon Database), and JWT Authentication.

This project was developed as part of a technical assessment for the Wheelson BizAI interview process to demonstrate frontend and backend development skills, API integration, database connectivity, authentication, and CRUD operations.

---

## Features

### User Authentication

* User Signup with Email and Password
* User Signin with JWT Authentication
* Password Encryption using Bcrypt
* Secure Route Access using JWT Token

### Todo Management

* Add New Tasks
* View All Tasks
* Mark Tasks as Completed
* Delete Tasks
* User-specific Task Management

### Frontend Features

* React Functional Components
* React Hooks (useState, useEffect)
* Form Validation
* API Integration using Axios
* Responsive and Clean UI

### Backend Features

* REST API Development using Express.js
* PostgreSQL Database Integration
* JWT Authentication Middleware
* Secure Password Storage

---

## Tech Stack

### Frontend

* React.js
* React Router DOM
* Axios
* HTML
* CSS

### Backend

* Node.js
* Express.js
* JWT
* Bcrypt

### Database

* PostgreSQL
* Neon Database

### Deployment

* Vercel (Frontend)
* Render / Railway (Backend)

---

## Project Structure

```bash
project-root
│
├── backend
│   ├── routes
│   │   ├── authRoutes.js
│   │   └── taskRoutes.js
│   ├── db.js
│   ├── server.js
│   └── package.json
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   │   ├── Signup.jsx
│   │   │   ├── Signin.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
│
└── README.md
```

---

## API Endpoints

### Authentication

#### Signup

```http
POST /api/auth/signup
```

Request Body:

```json
{
  "email": "user@gmail.com",
  "password": "123456"
}
```

---

#### Signin

```http
POST /api/auth/signin
```

Request Body:

```json
{
  "email": "user@gmail.com",
  "password": "123456"
}
```

---

### Tasks

#### Get Tasks

```http
GET /api/tasks
```

---

#### Add Task

```http
POST /api/tasks
```

Request Body:

```json
{
  "title": "Learn React"
}
```

---

#### Complete Task

```http
PUT /api/tasks/:id
```

---

#### Delete Task

```http
DELETE /api/tasks/:id
```

---

## Database Tables

### Users

| Column   | Type    |
| -------- | ------- |
| id       | SERIAL  |
| email    | VARCHAR |
| password | VARCHAR |

### Tasks

| Column    | Type    |
| --------- | ------- |
| id        | SERIAL  |
| title     | VARCHAR |
| completed | BOOLEAN |
| user_id   | INTEGER |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Backend Setup

```bash
cd backend
npm install
npm start
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Learning Outcomes

This project helped me understand:

* React Components
* React Hooks
* State Management
* API Integration
* Authentication using JWT
* PostgreSQL Database Connectivity
* CRUD Operations
* Full Stack Application Development

---

## Author

Sathish A

B.E. Computer Science and Engineering

2026 Graduate

Developed as part of the Wheelson BizAI Technical Assessment.
