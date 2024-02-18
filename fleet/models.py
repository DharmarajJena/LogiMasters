from django.db import models
from Users.models import Fleets,FleetManagers
# Create your models here.

class Notifications(models.Model):

    message=models.CharField(max_length=100)
    registration_no=models.CharField(max_length=20)
    seen=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="Notifications"

class LocationInfo(models.Model):

    fleet=models.ForeignKey(Fleets,on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fleet.registration_no}'s location at {self.timestamp}"
    
# class Device(models.Model):
#     firebase_token = models.CharField(max_length=255)
#     user=models.ForeignKey(FleetManagers,on_delete=models.CASCADE)

# class DrowsyDetails(models.Model):

#     timestamp= models.DateTimeField(auto_now=True)
#     fleet=models.ForeignKey(Fleets, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural="DrowsyDetails"