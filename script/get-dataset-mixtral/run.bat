echo.

Powershell.exe -ExecutionPolicy Bypass -Command "& {Start-Process PowerShell -ArgumentList '-noexit -noprofile -ExecutionPolicy Bypass -Command ""rclone copyurl %CM_RCLONE_WINDOWS_URL% . -a -P""'}" 

IF %ERRORLEVEL% NEQ 0 EXIT 1

echo CM_DATASET_PREPROCESSED_PATH=%CD%\%CM_DATASET_FILE_NAME% > tmp-run-env.out
echo %CD%\%CM_DATASET_FILE_NAME%
