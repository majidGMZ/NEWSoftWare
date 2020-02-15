from django.contrib import admin
from account.models import Account

# Register your models here.
from django.contrib.auth.admin import UserAdmin

admin.site.register(Account)

