import cv2
from google.colab.patches import cv2_imshow
from process_video import process_video
from transcribe_audio import transcribe_audio
from emotion_detection import emotion_detection
from display_emotion_results import display_emotion_results

def main():
    video_path = "video-1.mp4"
    print("Welcome to the Emotion Classifier!")
    print("Processing video...")
    frame_list, emotions_list, emotion_result = process_video(video_path)
    print(f"Most common emotion from video: {emotion_result}")
    for frame, emotion in zip(frame_list, emotions_list):
        if emotion == emotion_result:
            cv2.putText(frame, str(emotion_result), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
            cv2_imshow(frame)
            break

    print("Transcribing audio...")
    text_result = transcribe_audio(video_path)
    print(f"Transcription: {text_result}")
    print("Detecting emotion from transcription...")
    results = emotion_detection(text_result)
    display_emotion_results(results)

if __name__ == "__main__":
    main()
