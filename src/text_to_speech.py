from gtts import gTTS
import pygame
from io import BytesIO
import keyboard as kb
def speak(text):
    tts = gTTS(text, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    # Initialize pygame mixer and play the sound
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Wait until playback finishes
        pass