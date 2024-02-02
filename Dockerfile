FROM python:latest

WORKDIR /app

COPY dist/sql-injection/ .

COPY database.db .

EXPOSE 5000

CMD [ "./sql-injection" ]
