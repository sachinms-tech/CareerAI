# CareerAI 🚀

An AI-powered career assistance web application built with Django and Google Gemini.

CareerAI helps users explore career options, analyze resumes, and keep track of their previous career searches and resume analyses in one place.

## 🌐 Live Demo

http://127.0.0.1:8000/

## 📌 GitHub Repository

https://github.com/sachinms-tech/CareerAI

---

## ✨ Features

### 🔎 AI Career Search

Users can search for careers such as:

- Python Developer
- Data Analyst
- Web Developer
- Software Engineer
- Machine Learning Engineer

CareerAI uses Google Gemini to generate career-related information and guidance.

### 📄 Resume Analyzer

Users can upload a resume and analyze it through the application.

The application extracts resume text and stores the analysis history.

### 📚 History

CareerAI keeps track of:

- Previous career searches
- Resume analysis history
- Search timestamps
- Resume extraction status

### 🔐 User Authentication

The application includes:

- User registration
- User login
- User logout
- User-specific history

### 🤖 Google Gemini Integration

CareerAI integrates Google's Gemini API to provide AI-powered career responses.

The application is designed so that the API key is stored through environment variables rather than being hard-coded into the source code.

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Google Gemini API

### Frontend

- HTML
- CSS
- Django Templates

### Database

- SQLite

### Deployment

- Render

### Version Control

- Git
- GitHub

---

## 🏗️ Project Structure

```text
CareerAI/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── core/
│   ├── templates/
│   │   ├── history.html
│   │   └── ...
│   │
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
