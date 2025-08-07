# Cash Flow Tracker

Веб-приложение для учёта движения денежных средств. Реализовано на Django и Django REST Framework.

## Локальный запуск (без Docker)

1. Скопируйте файл `.env.dev.example` в `.env` и при необходимости отредактируйте переменные.
2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Примените миграции и при желании загрузите тестовые данные:

   ```bash
   python manage.py migrate
   python manage.py loaddata fixtures/initial_data.json  # опционально
   ```

4. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

По умолчанию используется SQLite. Чтобы подключить Postgres в разработке, задайте переменную `DATABASE_URL` в файле `.env`.

Документация API доступна по адресу `/api/docs/` после запуска сервера.

## Запуск через Docker

1. Скопируйте `.env.prod.example` в `.env` и укажите значения переменных окружения (секретный ключ, параметры БД).
2. Соберите и запустите контейнеры:

   ```bash
   docker compose up -d --build
   ```

   Миграции и сбор статики выполняются автоматически при старте контейнера.
3. Приложение будет доступно по адресу `http://localhost/`. Запросы к `/api/` извне блокируются nginx.

## Тесты

```bash
pytest
```

## Pre-commit

```bash
pre-commit install
pre-commit run --all-files
```
