"""
This module provides functions for performing emotion detection via IBM Watson NLP library.
"""
import requests, json

EMOTION_PREDICTION_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    Detects the emotions for a given text.

    Args:
        text_to_analyze (str): The text to be analyzed

    Returns:
        dict: A dictionary containing detected emotions and the dominant emotion.
    """

    json_body = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send the POST request to IBM Watson
        response = requests.post(EMOTION_PREDICTION_URL, json=json_body, headers = HEADERS)
        response.raise_for_status()
        response_json = response.json()
        
        # Handle empty emotionPredictions
        emotion_predictions = response_json.get('emotionPredictions', [])
        if len(emotion_predictions) <= 0:
            return {"error": "No emotion predictions found"}
        
        # Handle empty emotion
        emotion = emotion_predictions[0].get('emotion', {})
        if len(emotion) <= 0:
            return {"error": "No emotion found"}

        # Determine dominant emotion
        dominant_emotion = max(emotion, key=emotion.get)
        return {**emotion, **{'dominant_emotion': dominant_emotion}}

    except requests.exceptions.RequestException as e:
        print(f"Error: A RequestException occurred - {e}")
        raise