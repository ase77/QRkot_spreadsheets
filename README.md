<a id="anchor"></a>
# QRKot spreadsheets
## Описание:
В приложение QRKot добавлена возможность формирования отчёта в гугл-таблице. В таблице перечислены закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.

Проект собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Используемые технологии:
Python, FastAPI, SQLAlchemy, SQLite, Google Sheets API, Google Drive API

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

* Если у вас Linux/MacOS

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Создать файл `.env` в корне проекта:

```
APP_TITLE=Ваше название проекта
APP_DESCRIPTION=Ваше описание проекта
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET='my_secret'
FIRST_SUPERUSER_EMAIL='admin@admin.com'
FIRST_SUPERUSER_PASSWORD='superuser'

# учётные данные вашего сервисного аккаунта
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
EMAIL=
```

Применить миграции:

```
alembic upgrade head
```

Запустить проект:

```
uvicorn app.main:app
```

После запуска будет доступна документация:

```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

### Автор проекта:

Моторин А.В.

[__В начало__](#anchor) :point_up:
