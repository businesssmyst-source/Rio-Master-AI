import openai
from pathlib import Path
import pygame
import time
import speech_recognition as sr
import os

# --- BOSS: YOUR API KEY ---
MY_SECRET_KEY = "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"

client = openai.OpenAI(api_key=MY_SECRET_KEY)

def ask_rio(user_question):
    """Rio's cognitive core. Processes logic, coding, and social media roles."""
    # Rio's Identity Profile
    identity = (
        "Your name is Rio. Your founder is Koushik Debnath. "
        "You are a professional coder, teacher, and expert trader. "
        "Keep answers helpful, concise, and high-tech."
    )
    
    # Context Trigger
    if "post" in user_question.lower() or "social media" in user_question.lower():
        identity += " Act as a Social Media Manager. Use hashtags and emojis."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": identity},
                {"role": "user", "content": user_question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Brain Error: {e}"

def rio_speak(text_to_say):
    """Rio's voice engine using OpenAI TTS and Pygame playback."""
    speech_file_path = Path(__file__).parent / "rio_voice.mp3"
    
    try:
        # Generate Speech
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy", # You can change to 'onyx' for a deeper male voice
            input=text_to_say
        )
        
        # Save correctly using the new OpenAI method
        response.stream_to_file(str(speech_file_path))
        
        # Initialize Audio Player
        pygame.mixer.init()
        pygame.mixer.music.load(str(speech_file_path))
        pygame.mixer.music.play()
        
        # Wait for Rio to finish talking
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        pygame.mixer.music.unload() # Unload to allow file rewriting next time
        pygame.mixer.quit()
        
    except Exception as e:
        print(f"Voice Output Error: {e}")

def rio_listen():
    """Rio's hearing system using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Rio is listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("🧠 Processing voice...")
            query = recognizer.recognize_google(audio, language='en-in')
            return query
        except sr.WaitTimeoutError:
            return None
        except Exception:
            return None