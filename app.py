import streamlit as st
import os
import json
import openai
from brain import ask_rio
from emergency import get_emergency_report
from analyst import read_pdf, read_image_info
from manager import manage_trade, update_balance

# --- 🧠 BRAIN ACTIVATION: CONNECTING TO CLOUD SECRETS ---
# This line reaches into your "Secrets" vault to wake up Rio's AI brain
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- 1. PERMANENT DATA STORAGE ---
CONTACTS_FILE = "contacts.txt"
ACCOUNTS_FILE = "accounts.txt"

def save_login(data):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(data, f)

def load_login():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except:
            return {"Dad": "", "Mom": "", "Partner": ""}
    return {"Dad": "", "Mom": "", "Partner": ""}

# --- 2. SYSTEM INITIALIZATION ---
if 'sos_lock' not in st.session_state:
    st.session_state.sos_lock = False

st.set_page_config(page_title="RIO MASTER HUB", layout="wide", page_icon="🤖")

# --- 3. 3D CYBER THEME DESIGN ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXpueXpueXpueXpueXpueXpueXpueXpueXpueXpueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKMGpxvfJAsX89G/giphy.gif");
        background-size: cover; background-attachment: fixed;
    }
    .emergency-box {
        border: 3px solid #ff4b4b; padding: 20px; border-radius: 15px;
        background: rgba(100, 0, 0, 0.4); backdrop-filter: blur(10px);
        box-shadow: 0 0 20px #ff4b4b;
        color: white;
    }
    .stChatMessage { background: rgba(255, 255, 255, 0.05); border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: DATA & LOGIN ---
saved_ids = load_login()

with st.sidebar:
    if os.path.exists("rio_image.png"):
        st.image("rio_image.png", use_container_width=True)
    st.title("👤 RIO MASTER LOGIN")
    
    dad = st.text_input("Dad's ID:", saved_ids.get("Dad", ""))
    mom = st.text_input("Mom's ID:", saved_ids.get("Mom", ""))
    partner = st.text_input("Partner ID:", saved_ids.get("Partner", ""))
    
    if st.button("💾 SAVE LOGIN DATA", use_container_width=True):
        save_login({"Dad": dad, "Mom": mom, "Partner": partner})
        st.success("Rio has registered your family.")
    
    family_data = {"Dad": dad, "Mom": mom, "Partner": partner}
    
    st.write("---")
    st.subheader("📈 Trading Ledger")
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            st.text_area("Recent Activity:", f.read(), height=100)
    
    st.write("---")
    st.subheader("📁 Analyst Mode")
    uploaded_file = st.file_uploader("Upload PDF or Image", type=['pdf', 'png', 'jpg'])

# --- 5. MAIN INTERFACE ---
st.title("🤖 RIO MASTER CONTROL")
mode = st.selectbox("CHOOSE SPECIALIST MODE:", 
    ["General Chat", "🤖 RIO AI AUTOMATION", "📚 Study Mode", "💻 Coding Expert", "📈 Trading & Accounts"])

# --- 6. CHAT & BRAIN SYSTEM ---
user_input = st.chat_input("Command Rio...")

if user_input:
    st.session_state.sos_lock = False 
    
    # 1. Analyst Logic
    if "analyze" in user_input.lower() and uploaded_file:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if uploaded_file.name.lower().endswith(".pdf"):
            analysis = read_pdf(uploaded_file.name)
        else:
            analysis = read_image_info(uploaded_file.name)
        st.chat_message("assistant").write(analysis)
    
    # 2. Trading Logic
    elif "trade" in user_input.lower():
        trade_result = manage_trade(1000, 5) 
        st.chat_message("assistant").write(f"📊 {trade_result}")
        update_balance(trade_result)

    # 3. AI Brain Logic
    else:
        # Rio uses the brain mode selected to formulate an AI response
        response = ask_rio(f"In {mode} mode, answer this: {user_input}")
        st.chat_message("assistant").write(response)
    
    # 🔊 FIXED VOICE FEEDBACK (Mobile Friendly)
    if os.path.exists("rio_voice.mp3"):
        with open("rio_voice.mp3", "rb") as f:
            audio_bytes = f.read()
            st.audio(audio_bytes, format="audio/mp3")

# --- 7. SAFETY VAULT ---
st.write("---")
st.write("### 🛡️ Safety Vault")

if st.button("🚨 ACTIVATE EMERGENCY SOS", type="primary", use_container_width=True):
    st.session_state.sos_lock = True

if st.session_state.sos_lock:
    st.markdown('<div class="emergency-box">', unsafe_allow_html=True)
    st.subheader("⚠️ SOS ACTIVE")
    report = get_emergency_report(family_data)
    st.markdown(report)
    
    if st.button("✅ Resolve & Close SOS", use_container_width=True):
        st.session_state.sos_lock = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


st.caption("RIO AI - High Performance Safety & Productivity System | Founder: Koushik Debnath")
