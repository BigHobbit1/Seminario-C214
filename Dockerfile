# Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Baixa o script wait-for-it
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh -o /usr/local/bin/wait-for-it.sh && chmod +x /usr/local/bin/wait-for-it.sh

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD /usr/local/bin/wait-for-it.sh db:5432 -- uvicorn app.main:app --host 0.0.0.0 --port 8000
