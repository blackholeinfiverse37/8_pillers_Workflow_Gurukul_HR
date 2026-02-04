@echo off
echo ========================================
echo Karma Service - Clear Cache and Restart
echo ========================================
echo.

echo [1/3] Stopping any running Karma service...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *karma*" 2>nul
timeout /t 2 /nobreak >nul

echo [2/3] Clearing Python cache...
cd /d "%~dp0"
del /s /q __pycache__ 2>nul
del /s /q *.pyc 2>nul
for /d /r %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo Cache cleared!

echo [3/3] Starting Karma service...
echo.
echo Karma will run on http://localhost:8000
echo Press Ctrl+C to stop
echo.
python main.py
