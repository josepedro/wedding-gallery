FROM python:2.7.15

RUN apt-get update

# Debugging Tools
RUN apt-get install -y vim
RUN apt install -y htop

RUN apt-get install -y python-pip

COPY . weddinggallery

WORKDIR /weddinggallery

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic -v 3 --noinput

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
