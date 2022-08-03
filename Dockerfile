FROM python:3.8

WORKDIR /currency_api

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
