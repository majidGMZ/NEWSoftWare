from django.urls import path,re_path
from event import views

app_name = "event"




urlpatterns = [
    path('', views.EventListView, name='list_event'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('s/<int:pk>/',views.CommentOneEventDetailView.as_view(),name= 'comment_detail'),
    path('create/',views.EventCreateView.as_view(),name='event_create')
]
