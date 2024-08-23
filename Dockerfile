FROM python:3.12

WORKDIR /app

COPY ./app/ ./

RUN pip install -r ./requirements.txt

EXPOSE 5252

VOLUME /config
VOLUME /logs

ENV PORT=5252
ENV CONFIGPATH=/config/
ENV DATAPATH=/data/

ENV FLASK_ENV=production

CMD ["gunicorn", "app:app"]