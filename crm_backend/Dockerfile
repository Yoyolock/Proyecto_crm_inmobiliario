#Pulling an official base image
FROM python:3.11-alpine

#Setting work directory and structure
RUN mkdir /app
WORKDIR /app
COPY ./ /app
# # RUN chmod a+rwx -R /usr/media/

#Setting environment variables
#Equivalent to the pip install --disable-pip-version-check option
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
    # Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
    # Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
    # TimeZone
ENV TZ America/Santiago

#Installing psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --no-cache curl jq python3 py3-pip
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN apk --update --upgrade add musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add tzdata
RUN apk add --no-cache msttcorefonts-installer fontconfig
RUN update-ms-fonts
#Installing dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt --no-cache-dir
RUN ls

# # Adding and run as non-root user
RUN adduser -D user
USER user
# command: >
# sh -c "python manage.py makemigrations &&
# python manage.py migrate  &&
# gunicorn app.wsgi:application --bind 0.0.0.0:8000 --timeout 120 --workers 9"

