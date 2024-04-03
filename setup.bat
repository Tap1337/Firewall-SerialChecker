@echo off
echo Python -m pip install -r requirements.txt
cls
echo main.py >> Run.bat
start Run.bat
start /b "" cmd /c exit /b