import src.gemini_processor as gp
import src.speech_to_text as sr
import src.text_to_speech as tts
import keyboard as kb
import src.voice_action as va
from src.wake_up import WakeWordDetector
import time
import os



if __name__ == "__main__":
    # ACCESS_KEY = "Write your own"
    wake_word_detector = WakeWordDetector(access_key=os.getenv("ACCESS_KEY"),keywords=["computer"])
    wake_word_detector.start()

    try:
        
        while True:
            
            if wake_word_detector.listen():
                print("Wake word detected!")
                # Play wake-up sound
                tts.speak("How can I help you?")
                
                command = sr.listen()#imporve the speed o the voice rec after two to three commands

                if va.voice_action(command):  # TODO SOLVE SEARCH ISSUE IN SPOTIFY, calendar apply for developer mode
                    continue

                data = gp.response_by_gemini(command)
                tts.speak(data)
                
                 # Play sleep sound
                print("Going back to sleep...")
                time.sleep(1)  # Short delay before listening for wake word again
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        wake_word_detector.stop()

    


