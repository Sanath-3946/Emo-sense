# Emo-sense - A video based menatl health assessment

This project analyzes the emotions from a video by detecting faces and transcribing the audio. It uses DeepFace for facial emotion recognition, SpeechRecognition for audio transcription, and a transformer model for text-based emotion classification.

Minor Project Collaborated with https://github.com/bhavithareddy-05
## Project Structure

- `process_video.py`: Contains functions for processing video frames and detecting facial emotions.
- `transcribe_audio.py`: Contains functions for extracting and transcribing audio from the video.
- `emotion_detection.py`: Contains functions for emotion detection from text using a transformer model.
- `display_emotion_results.py`: Contains functions for displaying the emotion classification results.
- `main.py`: The main script to run the entire project.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/emotion_classifier.git
   cd emotion_classifier
