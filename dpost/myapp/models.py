from django.contrib.gis.db import models


# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location =  models.PointField(null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


 