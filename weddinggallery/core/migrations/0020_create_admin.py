import os
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_photo_likes'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_DB_NAME = 'default'
        DJANGO_SU_NAME = 'owner'
        DJANGO_SU_EMAIL = 'owner@owner.com'
        DJANGO_SU_PASSWORD = 'owner'

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]