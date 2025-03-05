from django.db import models

class ConfigSettings(models.Model):
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.name



