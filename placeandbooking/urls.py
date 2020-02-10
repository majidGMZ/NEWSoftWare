from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView

app_name = 'placeandbooking'

urlpatterns = [
    path('',views.index,name = 'indexView'),
    path('new_place/',views.CreatPlace.as_view(),name = 'newplace'),
    path('places/',views.IndexPlace.as_view(),name = 'places'),
    path('places/<int:pk>/',views.PlaceDetail.as_view(),name = 'place_detail'),
    path('search/',views.SearchResult.as_view(), name = 'search_place'),
    path('search/<int:pk>/',views.PlaceDetail_Search.as_view(),name = 'place_detail'),
    path('search/<int:pk>/Book',views.RegisterBooking.as_view(),name = 'send_request'),
    path('bookings/',views.BookingList.as_view(), name = 'bookings'),
    path('bookings/<int:pk>/',views.BookingDetail.as_view(), name = 'booking_detail'),
    path('placesbooking/',views.BookingsPlaceList.as_view(), name = 'place_booking'),
    path('placesbooking/<int:pk>/',views.BookingForPlace.as_view(),name = 'booking_for_place'),
    path('placesbooking/<int:place_id>/<int:pk>/',views.BookingDetailPlace.as_view(), name = 'book_detail'),
    path('update/<int:pk>/',views.HostAccept.as_view(),name = 'acceptance'),
    path('delete/<int:pk>/',views.HostDeleteBooking.as_view(), name = 'reject'),
]