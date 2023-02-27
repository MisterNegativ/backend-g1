from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    owner = models.CharField(max_length=255)

    def str(self):
        return self.title
