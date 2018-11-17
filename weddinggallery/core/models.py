from django.db import models

class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    status = models.CharField(max_length=10, blank=False, default='Approve')
