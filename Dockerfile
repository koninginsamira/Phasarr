FROM python:3.12

WORKDIR /

COPY ./ ./

# Install packages
RUN pip install -r ./requirements.txt
RUN rm -rf ./requirements.txt

# Generate Tailwind CSS
RUN cd ./phasarr && ./tailwindcss -i ./static/css/tailwind/input.css -o ./static/css/tailwind/output.css --minify
RUN cd ./phasarr && rm -rf ./tailwindcss ./tailwind.config.js ./static/css/tailwind/input.css

# Prepare entrypoint
RUN chmod a+x run.sh

EXPOSE 5252

VOLUME /config
VOLUME /logs

ENV DOCKER=1
ENV DEBUG=1
ENV LOG_LEVEL=info

ENV PORT=5252
ENV DEBUG_PORT=5678

ENV CONFIGPATH=config/
ENV DATAPATH=data/

ENTRYPOINT ["bash", "./run.sh"]