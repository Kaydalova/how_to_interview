<div align="center">
 <img src="interview_app/static/img/female_programmer_readme.png" alt="Logo"> 
<h3 >How to interview</h3>
Приложение поможет вам подготовиться к собеседованию на позицию Python-разработчик.
</div>

### Используемые технологии
- :snake: Python 3.8.10
- :incoming_envelope: Flask 2.0.2
- :rose: Jinja2 3.1.2
- :package: SQLAlchemy 1.4.29
- :memo: Alembic 1.7.7
### Описание проекта
Проект включает в себя:
- регистрацию и авторизацию
- личный кабинет со статистикой повторенных вопросов за каждый день
- блок с вопросами, разделенными по темам
- блок добавления своего вопроса (вопрос будет отправлен на модерацию админу и добавлен в базу после проверки)

Для лучшего запоминания рекомендуется уделять повторению вопросов 20 минут каждый день.

Приложение доступно по адресу http://31.129.96.219/

### Как запустить проект локально:
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

### Как запустить проект в контейнере:
Запустить контейнеры с базой данных и приложением
```
sudo docker compose up
```
Выполнить миграции, наполнить базу данных
```
docker exec -it how_to_interview-backend-1 bash
flask db migrate
flask db upgrade
flask load_questions
```


####  TODO:
- админка ✔️
- в личном кабинете пользователя список добавленных им вопросов ✔️
- расширить количество топиков и вопросов
- общий рейтинг пользователей
- запуск в докер ✔️
- запуск на сервере ✔️
