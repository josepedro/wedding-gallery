FROM python:2.7.15

RUN apt-get update

# Debugging Tools
RUN apt-get install -y vim
RUN apt install -y htop

RUN apt-get install -y python-pip

COPY . weddinggallery

WORKDIR /weddinggallery

ENV AWS_ACCESS_KEY_ID=AKIAJT6TDXOQ3VCT3VCA
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_STORAGE_BUCKET_NAME=sibtc-assets1

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic -v 3 --noinput

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
