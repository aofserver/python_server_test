# FROM python:3.11-alpine
FROM python:3.8-slim
# FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "server.py"]