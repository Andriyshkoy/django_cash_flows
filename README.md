# Cash Flow Tracker

Веб-приложение для учёта движения денежных средств. Реализовано на Django и Django REST Framework.

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json  # опционально, загрузка базовых данных
python manage.py runserver
```

Документация API доступна по адресу `/api/docs/` после запуска сервера.

## Тесты

```bash
pytest
```

## Pre-commit

```bash
pre-commit install
pre-commit run --all-files
```
