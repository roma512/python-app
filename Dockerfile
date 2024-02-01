FROM python:latest

WORKDIR /app

COPY dist/sql-injection/ .

COPY database.db .

COPY templates/ .

EXPOSE 5000

CMD [ "./sql-injection" ]
