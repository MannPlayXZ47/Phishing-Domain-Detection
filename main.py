import os
from flask import Flask, request, jsonify, render_template
import joblib
from utils.url_parser import URLParser

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(
    os.path.dirname(__file__), "utils/trained_models/phishing_model.pkl"
)
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data["url"]

    parser = URLParser(url)
    prediction = model.predict(parser.np_array())
    output = prediction[0].item()

    return jsonify({
        "prediction": output,
        "url": url,
        "message": (
            "Prediction says it's a phishing URL"
            if output == 1
            else "Prediction says it's a safe browsing URL"
        ),
    })

@app.route("/", methods=["GET", "POST"])
def predictui():
    if request.method == "GET":
        return render_template("index.html", prediction="", url=None)
    elif request.method == "POST":
        url = request.form["url"]
        try:
            parser = URLParser(url)
            prediction = model.predict(parser.np_array())
            output = prediction[0].item()

            message = (
                "Prediction says phishing URL"
                if output == 1
                else "Prediction says safe browsing URL"
            )
            return render_template("index.html", prediction=message, url=url)
        except Exception as e:
            return render_template("index.html", prediction="Invalid URL", url=url)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
