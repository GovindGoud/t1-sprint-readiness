FROM python:3.10

WORKDIR /app

RUN pip install requests

COPY mini_sprint.py .

CMD ["python", "mini_sprint.py"]
