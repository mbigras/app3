#!/usr/bin/env sh
# Entrypoint.sh launches Gunicorn server, then Gunicorn runs WSGI Flask app.

if [ -z "$PORT" ]
then
	PORT=8080
fi

if [ -d venv ]
then
	source venv/bin/activate
fi

exec gunicorn app:app --bind 0.0.0.0:$PORT
