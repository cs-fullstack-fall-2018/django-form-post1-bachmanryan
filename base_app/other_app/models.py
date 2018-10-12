from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateTimeField(default=timezone.now)

    def release(self):
        self.release_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
