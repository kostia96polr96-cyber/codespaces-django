FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    sqlite3 \
    nano

WORKDIR /var/www/app
COPY . .

RUN pip install -r requirements.txt && python manage.py collectstatic --noinput

RUN chmod -R 755 mycv/staticfiles/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mycv.wsgi:application"]
