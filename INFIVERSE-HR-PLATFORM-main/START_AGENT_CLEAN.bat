@echo off
echo Checking for processes on port 9000...

REM Kill any process using port 9000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :9000 ^| findstr LISTENING') do (
    echo Killing process %%a on port 9000...
    taskkill /F /PID %%a 2>nul
)

REM Wait for port to be released
timeout /t 2 /nobreak >nul

echo Starting HR Platform Agent on port 9000...
cd /d "%~dp0backend\services\agent"

REM Load environment variables from .env file
if exist .env (
    echo Loading environment variables from .env...
    for /f "usebackq tokens=1,* delims==" %%a in (".env") do (
        set "%%a=%%b"
    )
)

python -m uvicorn app:app --host 0.0.0.0 --port 9000
