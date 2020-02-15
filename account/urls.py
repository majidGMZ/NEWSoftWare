from django.urls import path, re_path
from account.views import Auth
from panel.views import Panel
from front.views import  Front

app_name = "account"

urlpatterns = [
    path('accounts/login', Auth.login),
    path('accounts/signup', Auth.singup),
    path('panel/submit_item', Panel.submit_item),
    path('panel/delete_item', Panel.delete_item),
    path('panel/edit_item', Panel.delete_item),
    path('panel/profile', Panel.profile),
    path('panel/verify', Panel.profile),
    path('panel/submit_comment', Panel.submit_comment),
    path('like', Panel.like),
    path('dislike', Panel.dislike),
    path('panel', Panel.home),
    path('spaces', Front.SpacesList),
    path('space', Front.Space),
    path('space', Front.Space),
]
