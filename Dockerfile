FROM alpine:3.14
WORKDIR /app
RUN apk add --update --no-cache python3==3.9.5-r2 \
	&& python3 -m venv venv \
	&& /app/venv/bin/pip install pip==22.0.3
COPY requirements.txt ./
RUN /app/venv/bin/pip install -r requirements.txt
COPY entrypoint.sh app.py ./

ARG APP
ARG VERSION
ARG COMMIT
ARG ENV

ENV APP=$APP
ENV VERSION=$VERSION
ENV COMMIT=$COMMIT
ENV ENV=$ENV

ENTRYPOINT ["/app/entrypoint.sh"]
