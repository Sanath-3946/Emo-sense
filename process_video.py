
#### `process_video.py`

```python
import cv2
from deepface import DeepFace
from collections import Counter

def process_video(video_path):
    frame_list = []
    emotions_list = []
    capture = cv2.VideoCapture(video_path)
    face_model = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = capture.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_model.detectMultiScale(gray_frame, 1.1, 5)

        for (x, y, w, h) in faces:
            emotions = DeepFace.analyze(frame[y:y+h, x:x+w], actions=["emotion"], enforce_detection=False)

            if emotions:
                dominant_emotion = emotions[0]["dominant_emotion"]
                emotions_list.append(dominant_emotion)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
            frame_list.append(frame)

    capture.release()
    emotion_counts = Counter(emotions_list)
    most_common_emotion = emotion_counts.most_common(1)[0][0]
    return frame_list, emotions_list, most_common_emotion
