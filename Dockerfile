FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /danil/django/test

COPY ./requirements.txt /danil/django/test
RUN pip install -r /danil/django/test/requirements.txt

COPY . /danil/django/test

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]