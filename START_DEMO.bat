@echo off
REM Foundation v3 Demo Launcher (Simple Version)

echo.
echo ========================================
echo    Foundation v3 Demo Launcher
echo ========================================
echo.

set /p company_name="Enter company name: "
set /p company_url="Enter company URL: "

echo.
echo Starting Foundation demo for %company_name%...
echo.

powershell -ExecutionPolicy Bypass -File "%~dp0START_FOUNDATION_DEMO.ps1" -CompanyName "%company_name%" -CompanyURL "%company_url%"

pause
