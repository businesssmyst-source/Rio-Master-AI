@echo off
title RIO SYSTEM LAUNCHER
echo -----------------------------------------
echo RIO MASTER SYSTEM STARTING...
echo Founder: Koushik Debnath
echo -----------------------------------------

:: 1. Launch the Web Hub in the background
start /min cmd /c "python -m streamlit run app.py"

:: 2. Launch the Voice Assistant in the foreground
echo [STATUS] Voice Assistant Loading...
python main.py

pause