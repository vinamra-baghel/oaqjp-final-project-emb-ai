from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_app():
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return "Error: Please provide", 400

    result = emotion_detector(text_to_analyze)

    if not result:
        return "Error: Emotion detection failed", 500

    output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return output

if __name__ == "__main__":
    app.run(debug=True, port=5000)
