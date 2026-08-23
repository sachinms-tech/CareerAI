# CareerAI 🚀

CareerAI is an AI-powered career assistance web application built with **Python, Django, and Google Gemini**.

The project helps users explore career options, receive AI-powered career guidance, analyze resumes, and maintain a history of their career searches and resume analyses.

---

## ✨ Features

### 🔎 AI Career Search

Search for careers such as:

- Python Developer
- Data Analyst
- Web Developer
- Software Engineer
- Machine Learning Engineer

CareerAI uses **Google Gemini** to generate career-related guidance and information.

---

### 📄 Resume Analyzer

Users can upload a resume and analyze it through the application.

The application extracts text from the uploaded resume and records the analysis in the user's history.

---

### 📚 History

CareerAI provides a history page containing:

- Previous career searches
- Career search timestamps
- Resume analysis history
- Resume extraction status

---

### 🔐 User Authentication

The application includes:

- User registration
- User login
- User logout
- User-specific history

---

### 🤖 Google Gemini Integration

CareerAI integrates the **Google Gemini API** to provide AI-powered career responses.

API credentials are stored through environment variables rather than being directly exposed in the source code.

---

## 🛠️ Technology Stack

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

### Version Control

- Git
- GitHub

### Deployment

- Render

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
