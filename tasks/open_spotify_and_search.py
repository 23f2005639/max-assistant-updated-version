import src.speech_to_text as sr
import src.text_to_speech as tts
import webbrowser
import pyautogui
import time

def open_spotify_and_search():
    # Open Spotify
    webbrowser.open("https://open.spotify.com")
    time.sleep(5)  # Wait for Spotify to open

    # Ask the user what to search for
    tts.speak("What music do you want to play?")
    search_query = sr.listen()

    # Use keyboard shortcuts to navigate to the search bar and type the search query
    pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar
    pyautogui.write("https://open.spotify.com/search")
    pyautogui.press('enter')
    time.sleep(3)  # Wait for the search page to load

    pyautogui.write(search_query)
    pyautogui.press('enter')