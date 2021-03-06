# from account.views import
# from django.contrib.auth import
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import localdate
from django.views import generic
from django.urls import reverse_lazy
from pytz import timezone

from placeandbooking import models
from django.contrib import messages
from account.models import Account


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
              'Price',
              ]

    success_url = reverse_lazy('event:list_event')

    def form_valid(self, form):
        account = Account.objects.get(pk = self.request.user.pk)
        form.instance.account = account
        return super().form_valid(form)

class EditPlace(generic.UpdateView):
    model = models.Place
    context_object_name = 'new_place'
    fields = ['Description',
              'PlacePhoto',
              'Pets',
              'Kids',
              'Price',
              ]
    success_url = reverse_lazy('event:list_event')

#shows all places available to rent
class IndexPlace(generic.ListView):
    model = models.Place
    template_name = 'placeandbooking/places_to_rent.html'
    context_object_name = 'places'

    def get_queryset(self):
        return models.Place.objects.all()

#show persons place detail
class PlaceDetail(generic.DetailView):
    models = models.Place
    template_name = 'placeandbooking/place_detail.html'
    context_object_name = 'place_detail'

    def get_queryset(self):
        return models.Place.objects.all()

#shows a persons places avalable to rent for travelers
class IndexPlace_for_person(generic.ListView):
    model = models.Place
    template_name = 'placeandbooking/places_to_rent_for_person.html'
    context_object_name = 'places'

    def get_queryset(self):
        account = self.request.user
        places = models.Place.objects.filter(account=account)
        return places

#show persons place detail
class PlaceDetail_for_person(generic.DetailView):
    models = models.Place
    template_name = 'placeandbooking/place_detail_for_person.html'
    context_object_name = 'place_detail'

    def get_queryset(self):
        return models.Place.objects.all()


class PlaceDetail_Search(generic.DetailView):
    models = models.Place
    template_name = 'placeandbooking/place_detail_search.html'
    context_object_name = 'place_detail'

    def get_queryset(self):
        return models.Place.objects.all()



class SearchResult(generic.ListView):
    models = models.Place
    template_name = 'placeandbooking/search_results.html'
    context_object_name = 'places'

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
    fields = ['Arrival','Depart']
    context_object_name = 'booking'
    template_name = 'placeandbooking/places_requested_for_rent.html'
    success_url = reverse_lazy('event:list_event')

    def form_valid(self, form):
        today = localdate()
        print(today)
        if form.instance.Arrival <= form.instance.Depart:
            if form.instance.Arrival >= today:
                place = models.Place.objects.get(pk = self.kwargs['pk'])
                form.instance.place = place
                form.instance.account = self.request.user
                return super().form_valid(form)
            return HttpResponse("<h2>invalid time input</h2>")
        elif form.instance.Arrival >= form.instance.Depart:
            messages.error(self.request, "Error")
            return HttpResponse("<h2>invalid time input</h2>")

#show the bookings for one place
class BookingList(generic.ListView):
    model = models.Booking

    # queryset = models.Booking.objects.filter(place__account=account)
    context_object_name = 'books'
    template_name = 'placeandbooking/Bookings.html'

    def get_queryset(self):
        account = self.request.user
        books = models.Booking.objects.filter(place__account=account)
        return books

class BookingDetail(generic.DetailView):
    model = models.Booking
    context_object_name = 'booked'
    template_name = 'placeandbooking/bookdetail.html'


class mybookings(generic.ListView):
    model = models.Booking
    context_object_name = 'books'
    template_name = 'placeandbooking/myBookings.html'

    def get_queryset(self):
        account = self.request.user
        book = models.Booking.objects.filter(account=account)
        return book

class mybookingdetail(generic.DetailView):
    model = models.Booking
    context_object_name = 'booked'
    template_name = 'placeandbooking/mybookdetail.html'

    def get_queryset(self):
        print(self.kwargs)
        return models.Booking.objects.filte()


class HostAccept(generic.UpdateView):
    model = models.Booking
    context_object_name = 'booking'
    fields = ['AcceptanceByHost']
    template_name = 'placeandbooking/places_requested_for_rent.html'
    success_url = reverse_lazy('event:list_event')


class HostDeleteBooking(generic.DeleteView):
    model = models.Booking
    success_url = reverse_lazy('event:list_event')