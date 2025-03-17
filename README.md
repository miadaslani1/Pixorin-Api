نحوه اجرای پروژه در لوکال هاست 
pip install django
pip install djangorestframework

حذف فولدر venv و قرار گرفتن در همان مسیر برای نوشتن دستورات دیگر در ترمینال 
python -m venv venv
cd venv
cd scripts
activate
pip install django
deactivate
cd ../../
cd pixorin-api
python manage.py runserver
