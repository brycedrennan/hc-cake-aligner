FROM python:3.7

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["python", "-m", "cake_aligner"]