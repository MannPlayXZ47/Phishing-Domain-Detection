# 🛡️ Phishing Domain Detection

This project is a Flask-based web application that detects whether a given URL is **phishing** or **safe** using machine learning and feature-based URL analysis.  
It uses a trained RandomForest model on features extracted from URLs.

---

## 🚀 Features

- Predicts if a URL is **safe** or **phishing**
- Web UI to input and test URLs
- Lightweight and fast
- Uses feature engineering with machine learning
- Clean code structure (`utils/`, `templates/`, `main.py`)

---

## 📦 Installation

Follow these steps to set up and run the project locally:

---

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/MannPlayXZ47/Phishing-Domain-Detection.git
cd Phishing-Domain-Detection
\`\`\`

---

### 2. Create and Activate Virtual Environment

#### On Windows:

\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

#### On macOS/Linux:

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

---

### 3. Install Dependencies

Make sure you have a `requirements.txt` file. Then run:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

To generate `requirements.txt` from your current environment:

\`\`\`bash
pip freeze > requirements.txt
\`\`\`

---

### 4. Run the Flask App

\`\`\`bash
python main.py
\`\`\`

Then open your browser and go to:

\`\`\`
http://127.0.0.1:5000
\`\`\`

---

## 📁 Project Structure

\`\`\`
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
\`\`\`

---

## 🙌 Contributing

Pull requests are welcome! If you'd like to add improvements, feel free to fork and submit a PR.
