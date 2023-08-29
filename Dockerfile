FROM python:alpine

RUN mkdir -p /usr/src/PythonApp

WORKDIR /usr/src/PythonApp

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]