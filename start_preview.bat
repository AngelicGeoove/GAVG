@echo off
title GAVG Website Preview Server
echo.
echo ========================================
echo    GAVG Website Preview Server
echo ========================================
echo.
echo Starting local server...
echo.

cd /d "%~dp0"

python preview.py

pause