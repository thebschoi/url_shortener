from django.db import models, connection


class Url(models.Model):
    link = models.URLField()
    new_link = models.URLField(default="")

    def __str__(self):
        return self.link