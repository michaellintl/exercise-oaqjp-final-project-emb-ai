from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.get("/")
def detect_emotion_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    
    if not text_to_analyze:
        return {"message": "Invalid input parameter"}, 400

    detection_result = emotion_detector(text_to_analyze)

    anger = detection_result.get('anger')
    disgust = detection_result.get('disgust')
    fear = detection_result.get('fear')
    joy = detection_result.get('joy')
    sadness = detection_result.get('sadness')
    dominant_emotion = detection_result.get('dominant_emotion')

    response_message = f"For the given statement, the system response is \
        'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \
        'joy': {joy} and 'sadness': {sadness}. The dominant emotion is \
        <strong>{dominant_emotion}</strong>."

    return response_message

if __name__ == "__main__":
    app.run(debug=True)
