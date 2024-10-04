@echo off

cd "%CM_GIT_CHECKOUT_PATH%"
git pull
git add *

REM Check if the CM_MLPERF_INFERENCE_SUBMISSION_DIR variable is set
if defined CM_MLPERF_INFERENCE_SUBMISSION_DIR (
    robocopy "%CM_MLPERF_INFERENCE_SUBMISSION_DIR%" "%CM_GIT_CHECKOUT_PATH%" /MIR
    git add *
)

REM Check if the previous command was successful
if %errorlevel% neq 0 exit /b %errorlevel%

git commit -a -m "%CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE%"
git push

REM Check if the previous command was successful
if %errorlevel% neq 0 exit /b %errorlevel%
