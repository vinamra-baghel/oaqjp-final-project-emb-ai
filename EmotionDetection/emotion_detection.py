import requests
import json

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Analyzes the emotional content of a given text using IBM Watson's Emotion Analysis service.

    Args:
    text_to_analyze (str): The text to be analyzed.

    Returns:
    dict: A dictionary containing the emotion scores. The keys are the emotions ('anger', 'disgust', 'fear', 'joy', 'sadness')
          and the values are the corresponding scores. The 'dominant_emotion' key indicates the emotion with the highest score.

    Raises:
    requests.exceptions.RequestException: If there is an error in the API request.
    """
    
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_text = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # try:
    response = requests.post(url, headers=headers, json=input_text, timeout=5)
    response.raise_for_status()
    status_code = response.status_code
    if status_code == 400:
        scores = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            'dominant_emotion': None
        }
    else:
        result = json.loads(response.text)
        scores = result['emotionPredictions'][0]['emotion']
        scores['dominant_emotion'] = max(scores, key = scores.get)
    # except requests.exceptions.RequestException as e:
    #     print(f"API request failed: {e}")
    #     return None
    
    return scores

if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))