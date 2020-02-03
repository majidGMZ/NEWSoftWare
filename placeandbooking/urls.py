from django.urls import path
from . import views


urlpatterns = [
    path('new_place/',views.CreatPlace.as_view(),name = 'newplace')
]