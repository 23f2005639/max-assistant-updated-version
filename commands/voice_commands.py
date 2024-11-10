import tasks.browser_control as bc
import tasks.open_spotify_and_search as oss

def open_browser():
    bc.open_browser_and_search()

def open_spotify_and_search():
    oss.open_spotify_and_search()

commands_for_voice = [
    {
        "keywords": ["open", "browser"],
        "action": open_browser,
    },{
        "keywords":["play","music"],
        "action": open_spotify_and_search,
    }
]
