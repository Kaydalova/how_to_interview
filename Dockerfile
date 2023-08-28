FROM python:3.8

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Копирование исходного кода приложения
COPY . /app

CMD ["gunicorn", "interview_app:app", "-b", "0.0.0.0:5000"]