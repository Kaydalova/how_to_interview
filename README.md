<div align="center">
    <img src="https://github.com/Kaydalova/how_to_interview/interview_app/static/img/female_programmer.png">
<h3 align="center">How to interview</h3>
</div>
Приложение поможет вам подготовиться к собеседованию на позицию Python-разработчик.

### Используемые технологии
- :snake: Python 3.8.10
- :incoming_envelope: Flask 2.0.2
- :busts_in_silhouette: Jinja2 3.1.2
- :package: SQLAlchemy 1.4.29
- :memo: Alembic 1.7.7
### Описание проекта
Проект включает в себя:
- регистрацию и авторизацию
- личный кабинет со статистикой повторенных вопросов за каждый день
- блок с вопросами, разделенными по темам
- блок добавления своего вопроса (вопрос будет отправлен на модерацию админу и добавлен в базу после проверки)

Для лучшего запоминания рекомендуется уделять повторению вопросов 20 минут каждый день.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone github.com/Kaydalova/how_to_interview
```

```
cd how_to_interview
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создадим и наполним базу данных:

```
flask create_db
flask load_questions
```
Запустим проект:
```
flask run
```
После запуска сервис будет доступен по адресу:
 http://127.0.0.1:5000


####  TODO:
- админка
- в личном кабинете пользователя список добавленных им вопросов
- общий рейтинг пользователей
- запуск в докер