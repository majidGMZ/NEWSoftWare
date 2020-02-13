"""SoftWare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#a comment for test commit
#second comment for test2 commit

from django.contrib import admin
from django.urls import path,include
from account.views import Auth
from panel.views import Panel
from front.views import Front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('placeandbooking.urls'), name= 'bookingplace'),
    path('accounts/login', Auth.login, name = 'login'),
    path('accounts/signup', Auth.singup, name = 'signup'),
    path('panel/submit_item', Panel.submit_item, name = 'submit_item'),
    path('panel/delete_item', Panel.delete_item, name = 'delete_item'),
    path('panel/edit_item', Panel.delete_item, name = 'edit_item'),
    path('panel/profile', Panel.profile, name = 'profile'),
    path('panel/verify', Panel.profile, name = 'verify'),
    path('panel/submit_comment', Panel.submit_comment, name = 'submit_comment'),
    path('like', Panel.like),
    path('dislike', Panel.dislike),
    path('panel', Panel.home),
    path('spaces', Front.SpacesList),
    path('space', Front.Space),
]