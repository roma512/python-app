FROM python:latest

WORKDIR /app

COPY dist/ .

COPY database.db .

EXPOSE 5000

CMD [ "./sql-injection/sql-injection" ]
