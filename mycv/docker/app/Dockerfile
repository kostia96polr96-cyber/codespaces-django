FROM Python:3.11-slim

RUN apt-get update && apt-get install -y \
    sqlite3 \
    nano

WORKDIR /var/www/app
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:80", "mycv.wsgi:application"]