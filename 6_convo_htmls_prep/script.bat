@echo off

setlocal enabledelayedexpansion

set PYTHON_PATH=python
set CSV_FILE=sets.csv  
REM Specify your CSV file path here

REM Check if the CSV file exists
if not exist %CSV_FILE% (
    echo CSV file %CSV_FILE% not found!
    pause
    exit /b
)

REM Read the CSV file, skipping the first line (header)
for /f "skip=1 tokens=1,2,3,4,5 delims=, " %%A in (%CSV_FILE%) do (
    REM Extract the set number and numbers from each row
    set "set_number=%%A"
    set "num1=%%B"
    set "num2=%%C"
    set "num3=%%D"
    set "num4=%%E"

    REM Call the evaluator.py script with the set number and the extracted numbers as arguments
    call %PYTHON_PATH% evaluator.py !set_number! !num1! !num2! !num3! !num4!
)

pause

