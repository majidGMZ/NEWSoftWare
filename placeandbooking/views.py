from django.shortcuts import render
from django.views import generic


from placeandbooking import models



# Create your views here.
class CreatPlace(generic.CreateView):
    model = models.Place
    context_object_name = 'new_place'
    fields = ['City',
              'Address',
              'KindofHome',
              'RoomType',
              'Capacity',
              'Description',
              'PlacePhoto',
              'Pets',
              'Kids',
              'SmokingAllowed',
              ]

class IndexPlace(generic.ListView):
    models = models.Place
    template_name = 'placeandbooking/places_to_rent.html'
    context_object_name = 'places'

    def get_queryset(self):
        return models.Place.objects.all()

class PlaceDetail(generic.DeleteView):
    models = models.Place
    template_name = 'placeandbooking/place_detail.html'
    context_object_name = 'place_detail'

    def get_queryset(self):
        return models.Place.objects.all();