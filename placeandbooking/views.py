from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from placeandbooking import models,forms



# Create your views here.
def index(request):
    return render(request,'placeandbooking/search_place.html')

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
        return models.Place.objects.all()

class PlaceDetail_Search(generic.DeleteView):
    models = models.Place
    template_name = 'placeandbooking/place_detail_search.html'
    context_object_name = 'place_detail'

    def get_queryset(self):
        return models.Place.objects.all()



class SearchResult(generic.ListView):
    models = models.Place
    template_name = 'placeandbooking/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('city')
        pet = checkTorF(self.request.GET.get('pet'))
        kid = checkTorF(self.request.GET.get('kid'))
        smoke = checkTorF(self.request.GET.get('smoke'))
        object_list = models.Place.objects.filter(
            City=query,
            Kids=kid,
            Pets=pet,
            SmokingAllowed=smoke)
        return object_list

def checkTorF(input):
    if input == None:
        input = False
    else:
        input = True
    return input


class RegisterBooking(generic.CreateView):
    model = models.Booking
    model.placerelation = 'teh'
    fields = ['placerelation','Arrival','Depart']
    context_object_name = 'booking'
    template_name = 'placeandbooking/places_requested_for_rent.html'