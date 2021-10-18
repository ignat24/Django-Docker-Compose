FROM python:3.8 as builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update
RUN apt-get upgrade -y\
    && apt-get -y install postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.8

RUN mkdir -p /home/app

RUN groupadd app
RUN useradd -m -g app app -p PASSWPRD
RUN usermod -aG app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apt-get update \
    && apt-get install netcat -y
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.prod.sh $APP_HOME

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME 

USER app
RUN ["chmod", "+x", "/home/app/web/entrypoint.prod.sh"]
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
