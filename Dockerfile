FROM python:latest

WORKDIR /app

COPY dist/ .

COPY database.db .

EXPOSE 5000

CMD [ "./app/sql-injection" ]
