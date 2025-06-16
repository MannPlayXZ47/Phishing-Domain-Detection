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

1. **Clone this repo:**

```bash
git clone https://github.com/MannPlayXZ47/Phishing-Domain-Detection.git
cd Phishing-Domain-Detection
