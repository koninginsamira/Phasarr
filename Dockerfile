FROM ubuntu:24.04
FROM python:3.12

WORKDIR /app

COPY ./app/ ./

RUN pip install -r ./phasarr/requirements.txt
RUN ./phasarr/tailwindcss -i ./phasarr/static/src/input.css -o ./phasarr/static/css/main.css --minify
RUN pip install -e .

RUN rm -rf ./phasarr/tailwindcss ./phasarr/tailwind.config.js ./phasarr/static/src/ ./phasarr/requirements.txt

RUN printf \
    "#!/bin/bash \
    \n\n \
    gunicorn phasarr:app --log-level=\${LOG_LEVEL}" \
> run.sh
RUN chmod +x run.sh

EXPOSE 5252

VOLUME /config
VOLUME /logs

ENV DOCKER=1
ENV FLASK_ENV=production
ENV LOG_LEVEL=info

ENV PORT=5252
ENV DEBUG_PORT=5678

ENV CONFIGPATH=config/
ENV DATAPATH=data/

ENTRYPOINT ["bash", "./run.sh"]