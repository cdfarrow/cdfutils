@ECHO OFF
REM Simple build commands for cdfutils

set PYTHON=py

REM Check that the argument is a valid command, and do it. /I ignores case.
FOR %%C IN ("Init"
            "RunTests"
            "Clean"
            "Build"
            "Publish") DO (
            IF /I "%1"=="%%~C" GOTO :Do%1
)
    
:Usage
    echo Usage:
    echo      make init
    echo      make runtests
    echo      make clean
    echo      make build
    echo      make publish
    exit

:DoInit
    %PYTHON% -m pip install -r requirements.txt
    exit
    
:DoRunTests
    %PYTHON% -m pytest
    exit

:DoClean
    rmdir /s /q ".\build"
    rmdir /s /q ".\dist"
    exit
    
:DoBuild
    @REM Build the wheel
    %PYTHON% -m build -w
    exit
    
:DoPublish
    echo Publishing wheel to PyPI
    %PYTHON% -m twine upload .\dist\cdfutils*
    exit


