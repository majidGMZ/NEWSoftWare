from django.db import models

# Create your models here.
from django.db.models import Choices
from django.utils.regex_helper import Choice


class Place(models.Model):

    roomtype=[('Private room', 'Private room'),
              ('Public room', 'Public room'),
              ]

    hometype =[('Apartment','Apartment'),
               ('Castle', 'Castle'),
               ('Cottage', 'Cottage')
               ]

    City = models.CharField(max_length= 15 )
    Address = models.CharField(max_length = 256)
    KindofHome=models.CharField(max_length= 15)
    RoomType = models.CharField(max_length= 15)
    Capacity = models.IntegerField()
    Description = models.TextField()
    PlacePhoto = models.ImageField(upload_to= 'placestaticfile',blank=True)

    #defult values when a place created
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

    placerelation = models.ForeignKey(Place,on_delete=models.CASCADE)
    Arrival = models.DateField()
    Depart = models.DateField()
    AcceptanceByHost = models.BooleanField(default=False)


    #to define wich user rented the home