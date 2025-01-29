@echo off
call D:\BPO\BPO-ABack\env\Scripts\activate 
:: La ruta de arriba cambia dependiendo de donde se encuentre el entorno virtual. En mi caso es en D:\BPO\BPO-ABack\env
python manage.py runserver 0.0.0.0:8000