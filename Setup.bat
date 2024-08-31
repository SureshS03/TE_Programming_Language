@echo off

SET SCRIPT_DIR=%~dp0

echo @echo off > %SCRIPT_DIR%TE.bat
echo python "%SCRIPT_DIR%src\main.py" %%1 >> %SCRIPT_DIR%TE.bat

COPY /Y "%SCRIPT_DIR%TE.bat" "C:\Windows\System32\TE.bat"

echo TE.bat has been set up successfully!
pause
