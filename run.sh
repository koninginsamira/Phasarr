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
export GEVENT_SUPPORT=True

echo Starting app...
exec gunicorn -k gevent phasarr:app --log-level="${LOG_LEVEL}"