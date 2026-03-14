from django.db import models

class Course(models.Model):

    title = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return self.title