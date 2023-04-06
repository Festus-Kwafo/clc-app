#Pull base image
FROM python:3.9

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install django dependencies
RUN pip install --upgrade pip
COPY requirements.txt /clc-app/
RUN pip install -r /clc-app/requirements.txt

#work directory
WORKDIR /clc-app/src

#install npm dependencies
RUN apt-get update && apt-get upgrade -y && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
apt-get install -y nodejs



COPY src/package*.json ./
RUN npm install

# Copy project
COPY . /clc-app/

#run webpack
COPY src/webpack.common.js /clc-app/src/
COPY src/webpack.prod.js /clc-app/src/

RUN npm run build

RUN python manage.py collectstatic --noinput --clear
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000


