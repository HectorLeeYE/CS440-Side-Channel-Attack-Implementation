FROM python:3.13.7-slim

WORKDIR /app

COPY server.py .
COPY requirements.txt .


RUN pip install -r requirements.txt
RUN python3 --version

EXPOSE 5000

CMD ["python3", "server.py"]