#!/bin/bash

while true; do
    flask --app phasarr db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

export FLASK_DEBUG=$DEBUG

echo Starting app...
exec gunicorn phasarr:app --log-level="${LOG_LEVEL}"