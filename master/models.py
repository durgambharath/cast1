from django.db import models

# Create your models here.


class CastDetails(models.Model):
    cast_Name = models.CharField(max_length=100)
    subcast_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cast_Name
