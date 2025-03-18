FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip pipenv curl && apt-get clean

WORKDIR /app
COPY . /app/
RUN pipenv install -r requirements.txt

EXPOSE 80

CMD pipenv run python3 main.py
