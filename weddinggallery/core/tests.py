from django.test import TestCase
from django.test import Client
from models import Photo

class WeddingGalleryTests(TestCase):

    def setUp(self):
        pass

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_photos(self):
        pass

    def test_approved_photos(self):
        pass

    def test_likes_photos(self):
        pass

    def test_sorted_photos_by_likes(self):
        pass

    def test_sorted_photos_by_upload_data(self):
        pass