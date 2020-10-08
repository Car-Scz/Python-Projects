from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=False)
    courseID = models.PositiveSmallIntegerField()
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(max_length=6)

    objects = models.Manager()

    def __str__(self):
        return self.title