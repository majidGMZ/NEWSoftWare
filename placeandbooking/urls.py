from django.urls import path
from . import views

app_name = 'placeandbooking'

urlpatterns = [
    path('new_place/',views.CreatPlace.as_view(),name = 'newplace'),
    path('places/',views.IndexPlace.as_view(),name = 'places'),
    path('places/<int:pk>/',views.PlaceDetail.as_view(),name = 'place_detail'),
]