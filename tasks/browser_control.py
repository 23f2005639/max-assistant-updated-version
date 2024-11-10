import src.gemini_processor as gp
import src.speech_to_text as sr
import src.text_to_speech as tts
import webbrowser
import pyautogui
import time

def open_browser_and_search():
    # Open the default browser
    webbrowser.open_new_tab("https://www.google.com")
    time.sleep(2)  # Wait for the browser to open

    # Ask the user what to search for
    tts.speak("What do you want to search for?")
    search_query = sr.listen()

    # Type the search query and press Enter
    pyautogui.write(search_query)
    pyautogui.press('enter')