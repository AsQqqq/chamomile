# Программа для автосервисной фирмы

## Установка

* Скачиваем проект
* Устанавливаем req.txt 
    * `pip install -r req.txt`
* Запускаем в корне такую команду:
    * `pyinstaller --noconfirm --onefile --windowed  --add-data "database.py;." --add-data "local.sqlite;." --add-data "serviceMain;." --add-data "serviceLogin;." --add-data "serviceClient.py;." --add-data "source_rc.py;."  "app.py"`