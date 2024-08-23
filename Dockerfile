FROM python:3.12

WORKDIR /app

COPY ./app/ ./

RUN pip install -r ./requirements.txt

ENV FLASK_ENV=production
ENV PORT=7272

EXPOSE 7272

CMD ["gunicorn", "app:app"]