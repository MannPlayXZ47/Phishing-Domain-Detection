# 🛡️ Phishing Domain Detection

This project is a machine learning-based web application that detects phishing domains using associative classification and feature engineering from URLs. It provides a simple interface to check if a given URL is **safe** or **phishing**.

---

## 🚀 Features

- 🔍 Accepts user-submitted URLs for prediction
- 🧠 Uses a trained Random Forest classifier
- 🔗 Extracts detailed URL features (IP count, redirect history, SSL certs, etc.)
- 🧰 Flask-based web interface for easy access
- ⚡ Fast and lightweight—no database or logging required in the lightweight version

---

## 🧠 Tech Stack

| Layer            | Tech Used                       |
|------------------|----------------------------------|
| Frontend         | HTML (via Flask Jinja templates) |
| Backend          | Python (Flask)                  |
| ML Model         | Random Forest (via scikit-learn) |
| Feature Parsing  | Custom URL feature extractor     |
| Packaging        | `joblib`                         |

---

## 📦 Installation

Follow these steps to set up and run the project locally:

---

### 1. Clone the Repository

```bash
git clone https://github.com/MannPlayXZ47/Phishing-Domain-Detection.git
cd Phishing-Domain-Detection
```

---

### 2. Create and Activate Virtual Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Make sure you have a `requirements.txt` file. Then run:

```bash
pip install -r requirements.txt
```

To generate `requirements.txt` from your current environment:

```bash
pip freeze > requirements.txt
```

---

### 4. Run the Flask App

```bash
python main.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
Phishing-Domain-Detection/
│
├── main.py
├── README.md
├── requirements.txt
├── templates/
│   └── index.html
├── utils/
│   ├── url_parser.py
│   └── trained_models/
│       └── phishing_model.pkl
```

---

## 🙌 Contributing

Pull requests are welcome! If you'd like to add improvements, feel free to fork and submit a PR.
