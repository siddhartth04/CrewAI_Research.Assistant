@echo off
echo Creating venv with correct Python 3.9...
"C:\Users\Siddharth\AppData\Local\Programs\Python\Python39\python.exe" -m venv venv
echo Activating...
call venv\Scripts\activate.bat
echo Python version:
python --version
echo.
echo Now run: pip install -r requirements.txt
pause