### Foodgram

«Продуктовый помощник». На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Как запустить проект:

- Установите Docker
- Клонируйте репозиторий
``` git clone https://github.com/Astaforkin/foodgram-project-react.git ```
- Создайте и заполните файл .env в корневой директории проекта
-- -
### Заполнение .env файла:

- POSTGRES_USER=foodgram_user
- POSTGRES_PASSWORD=foodgrampassword
- POSTGRES_DB=foodgram
- DB_HOST=db_food
- DB_PORT=5432
- SECRET_KEY='your_secret_key'
- ALLOWED_HOSTS='localhost,127.0.0.1'
- DEBUG=True
-- -
- Перейдите в дирректорию /backend
``` cd /backend ```
- Cоздайте и активируйте виртуальное окружение:
``` python3 -m venv venv ```
``` source env/bin/activate ```
``` python3 -m pip install --upgrade pip ```
- Установите зависимости из файла requirements.txt:
``` pip install -r requirements.txt ```
- Запустите docker-compose в корневой директории проекта командой
``` docker-compose up -d --build ```
- Выполните миграции
``` docker-compose exec backend python manage.py migrate ```
- Создайте суперпользователя
``` docker-compose exec backend python manage.py createsuperuser ```
- Для сбора статики воспользуйтесь командой
``` docker-compose exec backend python manage.py collectstatic ```
- Для загрузки базы данных ингрединтов
``` docker-compose exec backend python manage.py load_data ```
-- -
### Для доступа к сервису:
http://localhost:8000/

### Для доступа в админ-зону:
http://localhost:8000/admin
- Используйте данные суперпользователя
-- -
### Технологии:
- Python 3.9
- Django 3.2.3
- Django Rest Framework 3.14
- Docker 24.0.5
- Nginx 1.18
- Postgres 15.3
## Автор

[Астафоркин Никита](https://github.com/Astaforkin)
