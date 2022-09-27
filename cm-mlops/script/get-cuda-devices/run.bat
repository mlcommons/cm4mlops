rem Compile

del a.exe

echo.
echo Checking compiler version ...
echo.

%CM_NVCC_BIN% -V

echo.
echo Compiling program ...
echo.

cd %CM_TMP_CURRENT_SCRIPT_PATH%

%CM_NVCC_BIN% print_cuda_devices.cu -allow-unsupported-compiler -DWINDOWS
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

rem Return to the original path obtained in CM

echo.
echo Running program ...
echo.

cd %CM_TMP_CURRENT_PATH%

%CM_TMP_CURRENT_SCRIPT_PATH%\a.exe
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

