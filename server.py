from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion():
    text = request.form["text"]
    
    if text == "":
        return "Invalid input"
    
    result = emotion_detector(text)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
