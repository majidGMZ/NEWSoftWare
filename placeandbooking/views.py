from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from placeandbooking import models
from django.contrib import messages


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
    model = models.Place
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

class PlaceDetail_Search(generic.DetailView):
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
    fields = ['Arrival','Depart']
    context_object_name = 'booking'
    template_name = 'placeandbooking/places_requested_for_rent.html'
    success_url = reverse_lazy('placeandbooking:indexView')


    def form_valid(self, form):

        if form.instance.Arrival <= form.instance.Depart:
            place = models.Place.objects.get(pk = self.kwargs['pk'])
            form.instance.place = place
            return super().form_valid(form)

        elif form.instance.Arrival >= form.instance.Depart:
            messages.error(self.request, "Error")
            return super().form_invalid(form)



class BookingList(generic.ListView):
    model = models.Booking
    context_object_name = 'books'
    template_name = 'placeandbooking/Bookings.html'

class BookingDetail(generic.DetailView):
    model = models.Booking
    context_object_name = 'booked'
    template_name = 'placeandbooking/bookdetail.html'

class BookingsPlaceList(generic.ListView):
    model = models.Place
    template_name = 'placeandbooking/places_booked_list.html'
    context_object_name = 'place_book'

    '''in future should filter by user'''

class BookingForPlace(generic.ListView):
    model = models.Booking
    template_name = 'placeandbooking/booking_for_place.html'
    context_object_name = 'book_place'

    def get_queryset(self):
        pk = self.kwargs['pk']
        print(self.kwargs)
        object_list = models.Booking.objects.filter(place_id=pk)
        return object_list

class BookingDetailPlace(generic.DetailView):
    model = models.Booking
    context_object_name = 'booked'
    template_name = 'placeandbooking/placebookdetail.html'



class HostAccept(generic.UpdateView):
    model = models.Booking
    fields = ['AcceptanceByHost']
    template_name = 'placeandbooking/places_requested_for_rent.html'
    success_url = reverse_lazy('placeandbooking:indexView')

class HostDeleteBooking(generic.DeleteView):
    model = models.Booking
    success_url = reverse_lazy('placeandbooking:indexView')