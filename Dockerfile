FROM amd64/python:3.9-slim-buster

EXPOSE 8000

RUN apt-get update

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential

ADD . /course_enroll_django

WORKDIR /course_enroll_django

RUN pip3 install -r requirements.txt

RUN chmod +x manage.py

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]