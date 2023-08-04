
FROM python:3.8


WORKDIR /app


COPY requirements.txt manage.py /app/
COPY  . .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
