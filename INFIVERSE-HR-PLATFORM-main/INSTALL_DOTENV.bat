@echo off
echo Installing python-dotenv for environment variable loading...

cd /d "%~dp0backend\services\agent"
pip install python-dotenv

cd /d "%~dp0backend\services\gateway"
pip install python-dotenv

echo.
echo Installation complete!
echo.
echo Now restart your HR Platform services:
echo   - START_AGENT_CLEAN.bat
echo   - START_GATEWAY_CLEAN.bat
pause
