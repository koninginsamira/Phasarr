FROM ubuntu:24.04
FROM python:3.12

WORKDIR /app

COPY ./app/ ./

RUN pip install -r ./requirements.txt
RUN ./tailwindcss -i ./static/src/input.css -o ./static/css/main.css --minify

RUN rm -rf ./tailwindcss ./tailwind.config.js ./static/src/ ./requirements.txt

RUN printf \
    "#!/bin/bash \
    \n\n \
    gunicorn app:app --log-level=\${LOG_LEVEL}" \
> run.sh
RUN chmod +x run.sh

EXPOSE 5252

VOLUME /config
VOLUME /logs

ENV FLASK_ENV=production
ENV LOG_LEVEL=info

ENV PORT=5252
ENV DEBUG_PORT=5678

ENV CONFIGPATH=/config/
ENV DATAPATH=/data/

ENTRYPOINT ["bash", "./run.sh"]