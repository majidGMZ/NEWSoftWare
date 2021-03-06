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

# a comment for test commit
# second comment for test2 commit
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path,include

from SoftWare import settings
from account.views import Auth
from panel.views import Panel
from front.views import Front




urlpatterns = [

    path('admin/', admin.site.urls, name = 'admin'),
    path('', include('placeandbooking.urls'), name='bookingplace'),
    path('', include('event.urls'), name='event_project'),
    path('',include('account.urls'), name = 'account_url')
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
