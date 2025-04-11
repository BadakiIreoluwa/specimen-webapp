# Specimen Size Calculator Web App

This simple web application built with Flask calculates the actual specimen size based on the microscope size (in millimetres) and the total magnification. The user can choose to enter the total magnification directly or provide the eyepiece and objective magnifications, which are multiplied together. The results are stored in a local SQLite database.

---

## 📁 Project Structure

```
specimen_web/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # HTML template for the UI
├── static/
│   └── css/
│       └── styles.css   # External CSS file for styling
└── specimens.db         # SQLite database (auto-created)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/BadakiIreoluwa/specimen-webapp.git
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
python app.py
```

Then open your browser and go to:

[http://127.0.0.1:5000](http://127.0.0.1:5000)
