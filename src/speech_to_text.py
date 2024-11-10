import speech_recognition as sr


recognizer = sr.Recognizer()

def listen():
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    except sr.RequestError as e:
        print("Request Failed: ", e)