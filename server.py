"""Flask app for emotion detection via Watson API"""
import logging
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = app.logger

@app.route('/')
def index():
    """
    Renders the 'index.html' template.
    This function does not take any input parameters.

    Returns:
        render_template: A function that renders the 'index.html' template.
    """
    logger.debug("Rendering index.html")
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_app():
    """
    This function handles the emotion detection API endpoint. It retrieves the text to analyze from the request parameters,
    validates the input, and then calls the emotion_detector function to analyze the text.

    Parameters:
    request (object): The request object containing the parameters.

    Returns:
    str: A string containing the emotion analysis results or an error message.
    """

    text_to_analyze = request.args.get('textToAnalyze')
    logger.debug("Received request for /emotionDetector with textToAnalyze: '%s'", text_to_analyze)

    if not text_to_analyze:
        return "Error: Please provide"

    result = emotion_detector(text_to_analyze)

    if not result:
        return "Error: Emotion detection failed"

    if result['dominant_emotion'] is not None:
        output = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    else:
        output = "Invalid text! Please try again!"
    return output

if __name__ == "__main__":
    app.run(debug=True, port=4000)
