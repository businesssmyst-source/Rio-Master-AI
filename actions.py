import os
import subprocess
import webbrowser
import psutil

def open_app(command):
    cmd = command.lower().strip()
    
    # --- RIO'S MASTER WEB LIST ---
    web_sites = {
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "whatsapp": "https://web.whatsapp.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
        "linkedin": "https://www.linkedin.com",
        "gemini": "https://gemini.google.com",
        "chatgpt": "https://chat.openai.com",
        "github": "https://www.github.com",
        "google": "https://www.google.com"
    }

    # --- RIO'S PC APP LIST ---
    pc_apps = {
        "chrome": "chrome.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
        "calculator": "calc.exe",
        "notepad": "notepad.exe",
        "vlc": "vlc.exe",
        "spotify": "spotify.exe"
    }

    # 1. Check Web Sites
    if cmd in web_sites:
        webbrowser.open(web_sites[cmd])
        return f"Opening {cmd} for you, Founder Koushik."
    
    # 2. Check PC Apps
    if cmd in pc_apps:
        try:
            os.system(f"start {pc_apps[cmd]}")
            return f"Launching {cmd} now, Boss."
        except Exception as e:
            return f"System error launching {cmd}: {str(e)}"
    
    # 3. Smart Fallback: Google Search
    webbrowser.open(f"https://www.google.com/search?q={cmd}")
    return f"I couldn't find {cmd}, so I am searching Google for you."

def close_app(app_name):
    app_name = app_name.lower().strip()
    process_map = {
        "chrome": "chrome.exe",
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "powerpoint": "POWERPNT.EXE",
        "calculator": "Calculator.exe",
        "notepad": "notepad.exe",
        "spotify": "Spotify.exe"
    }
    
    target = process_map.get(app_name, app_name)
    found = False
    
    for proc in psutil.process_iter(['name']):
        try:
            if target.lower() in proc.info['name'].lower():
                proc.kill()
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
            
    if found:
        return f"All instances of {app_name} have been terminated, Founder."
    else:
        return f"I couldn't find {app_name} running."