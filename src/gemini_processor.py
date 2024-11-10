import google.generativeai as genai
import os 

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

def response_by_gemini(text):
    if "exit" in text:
        return "Goodbye!"
    response = model.generate_content(f"Dont include any emojies and any puntuation marks except fullstop and commas and answer this query:  {text}")
    return response.text