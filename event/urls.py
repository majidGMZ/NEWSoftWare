from django.urls import path, re_path
from event import views

app_name = "event"

urlpatterns = [
    path('event/', views.EventListView, name='list_event'),
   # path('event/<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('event/s/<int:pk>/', views.CommentOneEventDetailView.as_view(), name='comment_detail'),
    path('event/create/', views.EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', views.EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('event/home/', views.HomePageView.as_view(), name='home'),
    path('event/search/', views.SearchResultsView.as_view(), name='list_spa_city'),
    path('event/<int:id>/remove/', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('event/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('event/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('discussion/create/', views.DiscussionCreateView.as_view(), name='discussion_create'),
    path('discussion/<int:pk>/update/', views.DiscussionUpdateView.as_view(), name='discussion_update'),
    path('discussion/<int:id>/remove/', views.DiscussionDeleteView.as_view(), name='discussion_delete'),
    path('discussion/detail/<slug:city>', views.DiscussionListView, name='discussion_detail_city'),
    path('discussion/<int:pk>/', views.DiscussionDetailView.as_view(), name='discussion_detail'),
    path('discussion/comment/<int:pk>', views.add_comment_to_discussion, name='add_comment_to_discussion'),
    path('discussion/comment/<int:pk>/approve/', views.comment_discussion_approve, name='comment_discussion_approve'),
    path('discussion/comment/<int:pk>/remove/', views.comment_discussion_remove, name='comment_discussion_remove'),
    path('event/join/<int:pk>', views.Joinevent.as_view(), name='join_event'),
    path('event/left/<int:pk>',views.LeaveEvent.as_view(),name='leave'),
    path('index/', views.index, name='list_event'),
    path('myevents/', views.Events_I_joined.as_view(),name='my_event_list')

]
