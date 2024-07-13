# /**
#  * file: transcribe_audio.py
#  * type: Python program file
#  * date: 12_JULY_2024
#  * author: karbytes
#  * license: PUBLIC_DOMAIN
#  */

import speech_recognition as sr
from pydub import AudioSegment

# Path to the audio file
audio_path = "karbytes_at_warm_springs_bart_station_17_february_2023.mp3"

# Convert mp3 to wav
sound = AudioSegment.from_mp3(audio_path)
sound.export("converted.wav", format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Convert wav to audio data
with sr.AudioFile("converted.wav") as source:
    audio_data = recognizer.record(source)

# Recognize speech using CMU Sphinx (offline)
try:
    text = recognizer.recognize_sphinx(audio_data)
    print("Transcription: ", text)
except AttributeError as e:
    print("Recognizer object does not have 'recognize_sphinx' method. Error:", e)
except sr.UnknownValueError:
    print("CMU Sphinx could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from CMU Sphinx; {e}")
