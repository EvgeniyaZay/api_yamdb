# api_yamdb
# Описание:
```angular2html
Проект предназначен для взаимодействия с API социальной сети YaMDb.
```
# Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке
```angular2html
git clone 
```
```angular2html
cd api_yamdb
```
### Создать и активировать виртуальное окружение:
```angular2html
python3 -m venv venv
```
```angular2html
source/bin/activate
```
### Установить зависимости из файла requiremens.txt:
```angular2html
python3 -m pip install --upgrade pip
```
```angular2html
pip install -r requirements.txt
```
### Выполнить миграции:
```angular2html
python3 manage.py migrate
```
### Запустить проект:
```angular2html
python3 manage.py runserver
```
### Документация к API:
```angular2html
http://127.0.0.1:8000/redoc/
```
### Над проектом работали
- Дементьев Александр
- Зайцева Евгения
- Денисов Максим