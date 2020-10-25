from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    return '{0}'.format(filename)


class Post(models.Model):

    title = models.CharField(max_length=250)
    image = models.FileField(
        upload_to=user_directory_path)
    image_caption = models.CharField(
        max_length=100, default='')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
