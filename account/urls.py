from django.conf.urls.static import static
from django.urls import path, re_path

from SoftWare import settings
from account.views import Auth
from panel.views import Panel
from front.views import  Front


app_name = "account"

urlpatterns = [
    path('accounts/login', Auth.login, name = 'login'),
    path('accounts/signup', Auth.singup, name = 'signup'),
    path('accounts/logout', Auth.logout, name = 'logout'),
    path('panel/submit_item', Panel.submit_item, name = 'submit'),
    path('panel/delete_item', Panel.delete_item,name = 'delete'),
    path('panel/edit_item', Panel.delete_item, name = 'edit'),
    path('panel/profile', Panel.profile, name = 'profile'),
    path('panel/profile/edit_profile', Panel.edit_profile, name='edit-profile'),
    path('panel/profile/saveChanges', Panel.saveChanges, name='saveChanges'),
    path('panel/verify', Panel.profile, name = 'verify'),
    path('panel/submit_comment', Panel.submit_comment),
    path('like', Panel.like),
    path('dislike', Panel.dislike),
    path('panel', Panel.home),
    path('spaces', Front.SpacesList),
    path('space', Front.Space),
    path('space', Front.Space),
    path('panel/profile/upload_avatar', Panel.upload_avatar, name='image_upload'),
    path('success', Panel.success, name='success'),
   # path('panel/profile/display_avatar', Panel.display_avatar, name='profile_imgs'),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
