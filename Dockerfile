FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
