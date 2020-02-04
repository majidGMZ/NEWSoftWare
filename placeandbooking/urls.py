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
]