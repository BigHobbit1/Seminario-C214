# Dockerfile
FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta app para dentro do container (mantendo o nome "app")
COPY ./app /code/app

EXPOSE 8000

# Executa o app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
