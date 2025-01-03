import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        emotion_scores = emotion_detector("I am glad this happened")
        dominant_emotion = emotion_scores.get('dominant_emotion')
        self.assertEqual(dominant_emotion, "joy")

    def test_anger(self):
        emotion_scores = emotion_detector("I am really mad about this")
        dominant_emotion = emotion_scores.get('dominant_emotion')
        self.assertEqual(dominant_emotion, "anger")

    def test_disgust(self):
        emotion_scores = emotion_detector("I feel disgusted just hearing about this")
        dominant_emotion = emotion_scores.get('dominant_emotion')
        self.assertEqual(dominant_emotion, "disgust")
        
    def test_sadness(self):
        emotion_scores = emotion_detector("I am so sad about this")
        dominant_emotion = emotion_scores.get('dominant_emotion')
        self.assertEqual(dominant_emotion, "sadness")

    def test_fear(self):
        emotion_scores = emotion_detector("I am really afraid that this will happen")
        dominant_emotion = emotion_scores.get('dominant_emotion')
        self.assertEqual(dominant_emotion, "fear")

unittest.main()
