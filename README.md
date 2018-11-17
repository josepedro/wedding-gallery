# Wedding Gallery [![CircleCI](https://circleci.com/gh/josepedro/wedding-gallery/tree/master.svg?style=svg)](https://circleci.com/gh/josepedro/wedding-gallery/tree/master)

This problem can be composed by following User Stories:

- US 1: As site's owner, I want to allow my friends uploading photos because I want to see and store these photos; Acceptance Criteria: site's owner have to see a list of photos. [DONE]

- US 2: As site's owner, I want to controll the visibility of photos because I want to show seletected photos; Acceptance Criteria: site's owner have to approve and disapprove photos and site's visitors will see only approved photos. [DONE]

- US 3: As site's owner, I want to permit visitors to like photos because I want to see the more liked photos; Acceptance Criteria: visitors have to see the number of "likes" on each photo on gallery. [DONE]

- US 4: As visitor, I want to sort photos by total of likes because I want to see the most liked photos as initials elements; Acceptance Criteria: visitors have to see a list of sorted photos by total of likes, the top element will be with more likes. [DONE]

- US 5: As visitor, I want to sort photos by date of upload because I want to see the most novels photos as initials elements; Acceptance Criteria: visitors have to see a list of sorted photos by date of upload, the top element will be with more new. [DONE]

## Development Mode

We have to do following steps to developer mode:

- git clone https://github.com/josepedro/wedding-gallery.git && cd wedding-gallery

- pip install virtualenv

- virtualenv . -p /usr/bin/python2.7

- source bin/activate

- pip install -r requirements.txt

- python manage.py makemigrations

- python manage.py migrate

- python manage.py collectstatic

- python manage.py runserver

## Tests

All acceptance criterias are covered by tests in weddingggallery/core/tests.py module and can be run by using:

- python manage.py test weddinggallery

CircleCi was apllied in this project too.

## Deploy

First you have to install docker by following this link if you use ubuntu:

- https://docs.docker.com/install/linux/docker-ce/ubuntu

After to deploy:

- docker run -d -p 80:8000 -it josepedro/weddinggallery

The app will start a server on port 80. 

Also, you can see this application deployed at:

- http://ec2-18-234-37-217.compute-1.amazonaws.com

## Using Wedding Gallery Application

### Home Screen as Visitor

As visitor, you will see only photos that were approved by site's owner login (groom and bride access). 
You can upload images but you have to wait groom or bride to approve.

![Home Screen](images_demo/visitor_home.png)


