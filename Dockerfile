FROM python:3.10-alpine

ADD main.py .

RUN pip install re json beautifulsoup4 selenium flask

EXPOSE 5000

CMD ["python", "./main.py"]