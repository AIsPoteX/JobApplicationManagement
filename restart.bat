@echo off
echo.
echo [INFO] Starting Django Development Server...
echo.

echo [STEP 1/3] Making database migrations...
python manage.py makemigrations

echo.
echo [STEP 2/3] Applying database migrations...
python manage.py migrate

echo.
echo [STEP 3/3] Starting the server at http://127.0.0.1:8000/
python manage.py runserver

echo.
echo [INFO] Server has been stopped.
pause