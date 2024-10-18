echo %CM_RUN_CMD% 
call %CM_RUN_CMD%
if errorlevel 1 exit /b %errorlevel%
