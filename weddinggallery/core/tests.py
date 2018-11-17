from django.test import TestCase
from django.test import Client
from models import Photo

import os
from urlparse import urlparse

class WeddingGalleryTests(TestCase):

    def setUp(self):
        Photo.objects.create(
        	upload=os.path.basename(urlparse("https://sibtc-assets1.s3.amazonaws.com/media/pp.jpeg").path), 
        	status="Approve", likes=10)
        Photo.objects.create(
        	upload=os.path.basename(urlparse("https://sibtc-assets1.s3.amazonaws.com/media/pp_S7r54Yn.jpeg").path), 
        	status="Approve", likes=20)
        Photo.objects.create(
        	upload=os.path.basename(urlparse("https://sibtc-assets1.s3.amazonaws.com/media/pp_CLJBztL.jpeg").path), 
        	status="Disapprove", likes=30)

    def test_homepage(self):
        response = self.client.get('/')
    	photos = response.context[0]['photos']

    	self.assertEqual(photos[0].id, 1)
    	self.assertEqual(photos[1].id, 2)
    	self.assertEqual(photos[2].id, 3)
        self.assertEqual(response.status_code, 200)

    def test_photos(self):
    	response = self.client.get('/')
    	photos = response.context[0]['photos']

    	self.assertEqual(photos[0].upload.url, "https://sibtc-assets1.s3.amazonaws.com/media/pp.jpeg")
    	self.assertEqual(photos[1].upload.url, "https://sibtc-assets1.s3.amazonaws.com/media/pp_S7r54Yn.jpeg")
    	self.assertEqual(photos[2].upload.url, "https://sibtc-assets1.s3.amazonaws.com/media/pp_CLJBztL.jpeg")
        self.assertEqual(response.status_code, 200)

    def test_approved_photos(self):
        response = self.client.get('/')
    	photos = response.context[0]['photos']

    	self.assertEqual(photos[0].status, "Approve")
    	self.assertEqual(photos[1].status, "Approve")
    	self.assertEqual(photos[2].status, "Disapprove")
        self.assertEqual(response.status_code, 200)

    def test_likes_photos(self):
        response = self.client.get('/')
    	photos = response.context[0]['photos']

    	self.assertEqual(photos[0].likes, 10)
    	self.assertEqual(photos[1].likes, 20)
    	self.assertEqual(photos[2].likes, 30)
        self.assertEqual(response.status_code, 200)

    def test_sorted_photos_by_likes(self):
        response = self.client.get('/sort_like/')
    	photos = response.context[-1]['photos']

    	self.assertEqual(photos[2].likes, 10)
    	self.assertEqual(photos[1].likes, 20)
    	self.assertEqual(photos[0].likes, 30)
        self.assertEqual(response.status_code, 200)

    def test_sorted_photos_by_upload_data(self):
        response = self.client.get('/sort_upload/')
    	photos = response.context[-1]['photos']

    	self.assertEqual(photos[2].id, 1)
    	self.assertEqual(photos[1].id, 2)
    	self.assertEqual(photos[0].id, 3)
        self.assertEqual(response.status_code, 200)