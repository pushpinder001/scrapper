FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]