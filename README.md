# 📝 FastAPI To-Do API

A clean and structured RESTful To-Do List API built with FastAPI and
SQLAlchemy using Clean Architecture principles.

------------------------------------------------------------------------

## 🚀 Tech Stack

-   Python 3.13+
-   FastAPI
-   SQLAlchemy
-   SQLite
-   Pydantic
-   Uvicorn

------------------------------------------------------------------------

## 🏗 Project Structure

app/
│── main.py
│── database.py
│
├── models/
├── schemas/
├── repository/
├── service/
└── routers/

------------------------------------------------------------------------

## 🧠 Architecture Overview

This project follows a simplified Clean Architecture approach:

-   Router Layer → Handles HTTP requests
-   Service Layer → Contains business logic
-   Repository Layer → Manages database operations
-   Models → SQLAlchemy ORM models
-   Schemas → Pydantic validation models

------------------------------------------------------------------------

## 📌 Features

-   Create a new task
-   Retrieve all tasks
-   Update task status
-   Input validation using Pydantic
-   Business rule validation (duplicate prevention)
-   Dependency Injection using FastAPI

------------------------------------------------------------------------

## 🔗 API Endpoints

### GET /tasks

Returns all tasks.

### POST /task

Creates a new task.

Body: { "task": "Learn FastAPI" }

### POST /update/task

Updates task status.

Body: { "id":1, "is_done": true }

------------------------------------------------------------------------

## ▶️ How to Run

### Install dependencies

pip install -r requirements.txt

### Run server

uvicorn main:app --reload

Open: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 👨‍💻 Author

Youssef Eldeeb
