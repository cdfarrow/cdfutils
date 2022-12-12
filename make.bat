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
    echo      make init         - Install the libraries for building
    echo      make runtests     - Run the unit tests
    echo      make clean        - Clean out build files
    echo      make build        - Build the project
    echo      make publish      - Publish the project to PyPI
    goto :End

:DoInit
    %PYTHON% -m pip install -r requirements.txt
    %PYTHON% -m pip install -r requirements-dev.txt
    goto :End
    
:DoRunTests
    %PYTHON% -m pytest
    exit
    goto :End

:DoClean
    rmdir /s /q ".\build"
    rmdir /s /q ".\dist"
    goto :End
    
:DoBuild
    @REM Build the wheel (without using a virtual env)
    %PYTHON% -m build -w -n
    goto :End
    
:DoPublish
    echo Publishing wheel to PyPI
    %PYTHON% -m twine upload .\dist\cdfutils*
    goto :End


:End
