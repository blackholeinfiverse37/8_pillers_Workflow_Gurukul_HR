@echo off
echo Starting HR Platform Agent Service (Port 9000)...
echo.
echo IMPORTANT: Source files missing - using compiled bytecode
echo Running without --reload to prevent crashes
echo.

cd /d "%~dp0"

REM Check if .env exists
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please copy .env.corrected to .env first
    echo.
    pause
    exit /b 1
)

echo Starting agent service...
python -m uvicorn app:app --host 0.0.0.0 --port 9000

pause
