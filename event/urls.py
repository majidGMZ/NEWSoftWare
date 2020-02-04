from django.urls import path, re_path
from event import views

app_name = "event"

urlpatterns = [
    path('', views.EventListView, name='list_event'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('s/<int:pk>/', views.CommentOneEventDetailView.as_view(), name='comment_detail'),
    path('create/', views.EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='event_update'),
    path('home/search/', views.SearchResultsView.as_view(), name='event_search'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('home/search/<int:pk>/', views.EventDetailView.as_view(), name='detail_search'),
    path('<int:id>/remove/', views.EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
