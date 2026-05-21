FROM python:3.10-slim

# Устанавливаем ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запускаем сервер
CMD ["hypercorn", "main:app", "--bind", "[::]:8000"]
