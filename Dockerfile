FROM python:3.7-alpine

COPY src/ src/
COPY tests/ src/tests/

WORKDIR src

COPY setup.py .

RUN python setup.py develop

CMD [ "ash" ]
