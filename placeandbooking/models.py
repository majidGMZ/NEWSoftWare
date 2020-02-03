from django.db import models

# Create your models here.


class Place(models.Model):

    # roomtype=[('Private room', 'Private room'),
    #           ('Public room', 'Public room'),
    #           ]
    #
    # hometype =[('Apartment','Apartment'),
    #            ('Castle', 'Castle'),
    #            ('Cottage', 'Cottage')
    #            ]

    City = models.CharField(max_length= 15, null= False)
    Address = models.CharField(max_length = 256,null= False)
    KindofHome=models.CharField(max_length= 15,null= False)
    RoomType= models.CharField(max_length= 15,null= False)
    Capacity = models.PositiveIntegerField(null= False)
    Description = models.TextField(null= False)
    PlacePhoto = models.ImageField(upload_to= 'static',blank=True)

    #defult values when a place created will be false
    RequestedToRent = models.BooleanField(default = False,null= False)
    rented = models.BooleanField(default = False,null= False)

    #optional fileds
    Pets = models.BooleanField(default = False)
    Kids = models.BooleanField(default = False)
    SmokingAllowed = models.BooleanField(default = False)
    HostLanguage = models.CharField(max_length = 15,null= True)

    def __str__(self):
        return self.Address

class Booking(models.Model):

    placerelation = models.ForeignKey(Place,on_delete=models.CASCADE)
    Arrival = models.DateField(null=False)
    Depart = models.DateField(null=False)
    AcceptanceByHost = models.BooleanField(default=False,null=False)


    #to define wich user rented the home