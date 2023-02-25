FROM python:3.9.16-slim-bullseye
WORKDIR /scrapyrt/project

RUN apt-get update
RUN pip install --upgrade pip
COPY . /scrapyrt/project

RUN pip install -r requirements.txt
RUN playwright install-deps
RUN playwright install firefox

EXPOSE 9080

ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]