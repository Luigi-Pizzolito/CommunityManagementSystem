FROM python:3.8.3-slim-buster

COPY ./src/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /
COPY . .
ENTRYPOINT ["python", "/src/main.py"]