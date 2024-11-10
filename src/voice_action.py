import speech_recognition as sr
from commands.voice_commands import commands_for_voice as cv

def voice_action(command):  
        
        try:
            for cmd in cv:
                if all(keyword in command for keyword in cmd["keywords"]):
                    cmd["action"]()
                    return True
            return False
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Network error.")