# core/models.py

from django.db import models
# Create your models here.

class Movie(models.Model):
    DIFFICULTY_LEVELS = (
        ('Cartoons', 'Cartoons'),
        ('Comedy', 'Comedy'),
        ('romantic', 'romantic'),
    )
    name = models.CharField(max_length=120)
    definition = models.CharField(max_length=400)
    video = models.FileField()
    genre = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    country = models.TextField()

    def __str_(self):
        return "Movie for {}".format(self.name)