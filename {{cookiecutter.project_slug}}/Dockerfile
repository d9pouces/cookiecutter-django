FROM python:3.11
ENV PYTHONUNBUFFERED 1
ADD . /src/
WORKDIR /src
RUN python3 setup.py install
RUN python3 manage.py collectstatic --noinput
