FROM python:3.12

WORKDIR /app

COPY ./app/ ./

RUN pip install -r ./requirements.txt
RUN ./tailwindcss -i ./static/src/input.css -o ./static/css/main.css --minify

RUN rm -rf ./tailwindcss ./tailwind.config.js ./static/src/ ./requirements.txt

EXPOSE 5252

VOLUME /config
VOLUME /logs

ENV PORT=5252
ENV CONFIGPATH=/config/
ENV DATAPATH=/data/

ENV FLASK_ENV=production

CMD ["gunicorn", "app:app"]