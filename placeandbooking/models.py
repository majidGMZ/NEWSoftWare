from django.db import models

# Create your models here.


class Place(models.Model):


    City = models.CharField(max_length= 15)
    Address = models.CharField(max_length = 256)
    KindofHome=models.CharField(max_length= 15)
    RoomType= models.CharField(max_length= 15)
    Capacity = models.PositiveIntegerField()
    Description = models.TextField()
    PlacePhoto = models.ImageField(upload_to= 'static',blank=True)

    #defult values when a place created will be false
    RequestedToRent = models.BooleanField(default = False)
    rented = models.BooleanField(default = False)

    #optional fileds
    Pets = models.BooleanField(default = False)
    Kids = models.BooleanField(default = False)
    SmokingAllowed = models.BooleanField(default = False)
    HostLanguage = models.CharField(max_length = 15)

    def __str__(self):
        return self.Address

class Booking(models.Model):

    place = models.ForeignKey(Place,related_name="places",on_delete=models.CASCADE)
    Arrival = models.DateField(null=False)
    Depart = models.DateField(null=False)
    AcceptanceByHost = models.BooleanField(default=False)
    
    #to define wich user rented the home

    def __str__(self):
        x = self.pk
        return str(x)