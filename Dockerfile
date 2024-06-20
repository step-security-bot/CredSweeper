FROM python:3.10@sha256:bb4c63ac8c19ffbdb69dd7b62841fb5d76bde06c65cd031194f655d6747fa1d5

WORKDIR /app

ADD credsweeper /app/credsweeper

COPY pyproject.toml /app/
COPY README.md /app/

RUN pip install .

COPY entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
