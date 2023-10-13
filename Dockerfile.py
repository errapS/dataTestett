FROM python:3.11

RUN pip install pandas requests sqlalchemy schedule psycopg2-binary

COPY ./resources /app/resources

