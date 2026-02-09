@echo off
REM HR Platform Services Startup Script
REM Starts Gateway (8009), Agent (9000), and optionally LangGraph (9001)

echo ================================================================================
echo                    HR PLATFORM SERVICES STARTUP
echo ================================================================================
echo.

REM Check if services are already running
echo Checking for existing services...
netstat -ano | findstr ":8009" >nul
if %errorlevel% == 0 (
    echo [WARNING] Port 8009 already in use - Gateway may already be running
)

netstat -ano | findstr ":9000" >nul
if %errorlevel% == 0 (
    echo [WARNING] Port 9000 already in use - Agent may already be running
)

echo.
echo Starting HR Platform services...
echo.

REM Start Gateway Service (Port 8009)
echo [1/2] Starting HR Gateway on port 8009...
start "HR Gateway (8009)" cmd /k "cd /d INFIVERSE-HR-PLATFORM-main\backend\services\gateway && python -m uvicorn app.main:app --host 0.0.0.0 --port 8009"
timeout /t 3 /nobreak >nul

REM Start Agent Service (Port 9000)
echo [2/2] Starting HR Agent on port 9000...
start "HR Agent (9000)" cmd /k "cd /d INFIVERSE-HR-PLATFORM-main\backend\services\agent && python -m uvicorn app:app --host 0.0.0.0 --port 9000"
timeout /t 3 /nobreak >nul

echo.
echo ================================================================================
echo                    HR PLATFORM SERVICES STARTED
echo ================================================================================
echo.
echo Services:
echo   - HR Gateway:  http://localhost:8009/docs
echo   - HR Agent:    http://localhost:9000/docs
echo.
echo Optional:
echo   - HR LangGraph: http://localhost:9001/docs (not started by default)
echo.
echo To start LangGraph manually:
echo   cd INFIVERSE-HR-PLATFORM-main\backend\services\langgraph
echo   python -m uvicorn app.main:app --host 0.0.0.0 --port 9001
echo.
echo Press any key to run integration test...
pause >nul

REM Wait for services to fully start
echo.
echo Waiting for services to initialize (10 seconds)...
timeout /t 10 /nobreak >nul

REM Run integration test
echo.
echo Running integration test...
python test_hr_integration.py

echo.
echo Press any key to exit...
pause >nul
