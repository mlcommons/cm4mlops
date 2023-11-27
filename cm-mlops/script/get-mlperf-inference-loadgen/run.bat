﻿@echo off

echo =======================================================

set CUR_DIR=%cd%
echo Current path in CM script: %CUR_DIR%

if "%CM_MLPERF_INFERENCE_LOADGEN_DOWNLOAD%" == "YES" (
  set CM_MLPERF_INFERENCE_SOURCE=%CM_EXTRACT_EXTRACTED_PATH%
)

echo.
echo Switching to %CM_MLPERF_INFERENCE_SOURCE%\loadgen

cd %CM_MLPERF_INFERENCE_SOURCE%\loadgen
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo.
echo Running %CM_PYTHON_BIN% setup.py develop

%CM_PYTHON_BIN% setup.py develop
IF %ERRORLEVEL% NEQ 0 EXIT %ERRORLEVEL%

echo =======================================================
