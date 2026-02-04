@echo off
echo ========================================
echo Starting 9-Pillar BHIV System
echo ========================================
echo.

echo [1/9] Starting Karma (Port 8000)...
start "Karma" cmd /k "cd karma_chain_v2-main && python main.py"
timeout /t 10 /nobreak >nul

echo [2/9] Starting Bucket (Port 8001)...
start "Bucket" cmd /k "cd BHIV_Central_Depository-main && python main.py"
timeout /t 10 /nobreak >nul

echo [3/9] Starting Core (Port 8002)...
start "Core" cmd /k "cd v1-BHIV_CORE-main && python mcp_bridge.py"
timeout /t 10 /nobreak >nul

echo [4/9] Starting Workflow Executor (Port 8003)...
start "Workflow" cmd /k "cd workflow-executor-main && python main.py"
timeout /t 10 /nobreak >nul

echo [5/9] Starting UAO (Port 8004)...
start "UAO" cmd /k "cd ""Unified Action Orchestration"" && python action_orchestrator.py"
timeout /t 10 /nobreak >nul

echo [6/9] Starting Insight Core (Port 8005)...
start "Insight Core" cmd /k "cd insightcore-bridgev4x-main && python insight_service.py"
timeout /t 10 /nobreak >nul

echo [7/9] Starting Insight Flow Bridge (Port 8006)...
start "Insight Flow Bridge" cmd /k "cd Insight_Flow-main && start_bridge_standalone.bat"
timeout /t 10 /nobreak >nul

echo [8/9] Starting Insight Flow Backend (Port 8007 - Optional)...
start "Insight Flow Backend" cmd /k "cd Insight_Flow-main && start_insight_flow_fixed.bat"
timeout /t 10 /nobreak >nul

echo [9/9] Starting Gurukul Backend (Port 3000)...
start "Gurukul" cmd /k "cd gurukul-backend--main\backend && python -m app.main"
timeout /t 10 /nobreak >nul

echo.
echo ========================================
echo All 9 services started!
echo ========================================
echo.
echo Service Status:
echo   Karma:              http://localhost:8000/health
echo   Bucket:             http://localhost:8001/health
echo   Core:               http://localhost:8002/health
echo   Workflow:           http://localhost:8003/healthz
echo   UAO:                http://localhost:8004/docs
echo   Insight Core:       http://localhost:8005/health
echo   Insight Flow:       http://localhost:8006/health
echo   Insight Backend:    http://localhost:8007/health
echo   Gurukul:            http://localhost:3000/health
echo.
echo Press any key to exit...
pause >nul
