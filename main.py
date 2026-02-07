import json
import os
from brain import ask_rio, rio_speak, rio_listen
from actions import open_app, close_app
from emergency import get_emergency_report # Fixed function name
from analyst import read_pdf, read_image_info
from manager import manage_trade, update_balance

# --- 1. DATA SYNC (Shared with app.py) ---
CONTACTS_FILE = "contacts.txt"

def load_family_data():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except:
            return {"Dad": "Not Set", "Mom": "Not Set", "Partner": "Not Set"}
    return {"Dad": "Not Set", "Mom": "Not Set", "Partner": "Not Set"}

def start_rio():
    print("--- RIO AI MASTER SYSTEM: VOICE COMMAND ONLINE ---")
    print("Founder: Koushik Debnath")
    rio_speak("Hello Founder Koushik. I am monitoring all systems.")

    while True:
        # Step 1: Rio listens for your voice
        user_voice = rio_listen()
        
        if user_voice:
            user_text = user_voice.lower()
            print(f"You said: {user_text}")

            # --- 1. EMERGENCY MODE (Safety Logic) ---
            if "emergency" in user_text or "help me" in user_text:
                print("!!! EMERGENCY DETECTED !!!")
                rio_speak("Emergency mode activated. Tracking your location now.")
                
                # Sync with the saved IDs from your Web App
                family_data = load_family_data()
                alert_info = get_emergency_report(family_data) # Fixed function call
                
                print(alert_info)
                rio_speak("I have generated your GPS report and alerted your family. Stay safe, Koushik.")
                continue

            # --- 2. TRADING MANAGER ---
            elif "calculate trade" in user_text:
                rio_speak("Processing risk management.")
                # Uses manage_trade from manager.py
                risk_msg = manage_trade(1000, 2) 
                print(f"Rio: {risk_msg}")
                rio_speak(risk_msg)

            # --- 3. ANALYST MODE ---
            elif "analyze pdf" in user_text:
                rio_speak("Reading study document.")
                content = read_pdf("study.pdf")
                if "Error" in content:
                    rio_speak("I could not find study dot P D F.")
                else:
                    summary = ask_rio("Summarize this: " + content[:1000])
                    rio_speak("Here is the summary: " + summary)

            # --- 4. APP CONTROL ---
            elif "open" in user_text:
                app = user_text.replace("open", "").strip()
                result = open_app(app)
                rio_speak(result)
            
            elif "close" in user_text:
                app = user_text.replace("close", "").strip()
                result = close_app(app)
                rio_speak(result)

            # --- 5. SYSTEM EXIT ---
            elif "exit" in user_text or "stop rio" in user_text:
                rio_speak("System shutdown. Goodbye, Founder.")
                break
            
            # --- 6. GENERAL AI BRAIN ---
            else:
                answer = ask_rio(user_text)
                print(f"Rio: {answer}")
                rio_speak(answer)
        else:
            continue

if __name__ == "__main__":
    start_rio()