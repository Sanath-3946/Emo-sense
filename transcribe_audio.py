from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    output_audio_path = "opaudio.mp3"
    audio_clip.write_audiofile(output_audio_path, codec='mp3', ffmpeg_params=["-ar", "16000", "-ac", "1"])
    video_clip.close()
    audio_clip.close()
    sound = AudioSegment.from_mp3(output_audio_path)
    sound.export("transcript.wav", format="wav")
    AUDIO_FILE = "transcript.wav"
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    return text
