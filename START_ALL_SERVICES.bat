@echo off
echo ========================================
echo STARTING ALL SERVICES IN CORRECT ORDER
echo ========================================
echo.

echo [Step 1/4] Starting Karma on Port 8000...
start "Karma (Port 8000)" cmd /k "cd karma_chain_v2-main && python main.py"
timeout /t 10 /nobreak >nul

echo [Step 2/4] Starting Bucket on Port 8001...
start "Bucket (Port 8001)" cmd /k "cd BHIV_Central_Depository-main && python main.py"
timeout /t 10 /nobreak >nul

echo [Step 3/4] Starting Core on Port 8002...
start "Core (Port 8002)" cmd /k "cd v1-BHIV_CORE-main && python mcp_bridge.py"
timeout /t 10 /nobreak >nul

echo [Step 4/4] Starting Workflow Executor on Port 8003...
start "Workflow (Port 8003)" cmd /k "cd workflow-executor-main && python main.py"
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo ALL SERVICES STARTED!
echo ========================================
echo.
echo Verify in browser:
echo - Karma:    http://localhost:8000/docs
echo - Bucket:   http://localhost:8001/health
echo - Core:     http://localhost:8002/health
echo - Workflow: http://localhost:8003/docs
echo.
pause
