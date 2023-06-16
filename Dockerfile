FROM python:3.9-alpine

WORKDIR /app
COPY requerimientos.txt .
RUN pip install -r requerimientos.txt
COPY . ./src

CMD python src/manage.py runserver 0.0.0.0:8000
