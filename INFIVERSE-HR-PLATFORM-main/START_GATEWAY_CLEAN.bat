@echo off
echo Checking for processes on port 8009...

REM Kill any process using port 8009
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8009 ^| findstr LISTENING') do (
    echo Killing process %%a on port 8009...
    taskkill /F /PID %%a 2>nul
)

REM Wait for port to be released
timeout /t 2 /nobreak >nul

echo Starting HR Platform Gateway on port 8009...
cd /d "%~dp0backend\services\gateway"

REM Load environment variables from .env file
if exist .env (
    echo Loading environment variables from .env...
    for /f "usebackq tokens=1,* delims==" %%a in (".env") do (
        set "%%a=%%b"
    )
)

python -m uvicorn app.main:app --host 0.0.0.0 --port 8009
