from django.urls import path
from . import views
from django.views.generic.dates import ArchiveIndexView

app_name = 'placeandbooking'

urlpatterns = [
    # path('',views.index,name = 'indexView'),
    path('add_place/',views.CreatPlace.as_view(),name = 'newplace'),
    # path('all_places/',views.IndexPlace.as_view(),name = 'places'),
    path('all_places/<int:pk>/',views.PlaceDetail.as_view(),name = 'place_detail'),
    path('search/',views.SearchResult.as_view(), name = 'search_place'),
    path('search/<int:pk>/',views.PlaceDetail_Search.as_view(),name = 'place_detail'),
    path('search/<int:pk>/Book',views.RegisterBooking.as_view(),name = 'send_request'),
    path('bookings/',views.BookingList.as_view(), name = 'bookings'),
    # path('bookings/<int:pk>/',views.BookingDetail.as_view(), name = 'booking_detail'),
    path('mybooking/',views.mybookings.as_view(), name = 'my_bookings'),
    # path('mybooking/<int:pk>',views.mybookingdetail.as_view(),name = 'my_booking_detail'),
    path('update/<int:pk>/',views.HostAccept.as_view(),name = 'acceptance'),
    path('delete/<int:pk>/',views.HostDeleteBooking.as_view(), name = 'reject'),
    path('myplace/',views.IndexPlace_for_person.as_view(),name = 'person_place'),
    path('myplace/<int:pk>',views.PlaceDetail_for_person.as_view(),name = 'person_place_detail'),
    path('myplace/<int:pk>/update/',views.EditPlace.as_view(), name = 'edit_place')
]