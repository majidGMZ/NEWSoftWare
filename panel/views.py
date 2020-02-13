from django.shortcuts import render
from account.forms import UserCreationForm, LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from pprint import pprint
from django.core.mail import EmailMessage
import smtplib
from account.models import Spaces
from account.models import SpaceRank
from account.models import Comments
from django.shortcuts import redirect
import random
from django.db.models import Sum
import string


class Panel:
    @login_required(login_url='/signin')
    def home(self):
        addresses = Spaces.objects.filter(user_id=self.user.id)  # values_list('address', flat=True)
        return render(self, 'panel.html', {'addresses': addresses})

    @login_required(login_url='/signin')
    def verify(self):
        if self.user.link == self.GET['link']:
            self.user.is_verified = True
            self.user.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('failed')

    @login_required(login_url='/signin')
    def submit_comment(self):
        if self.method == 'POST':
            comment = Comments()
            comment.user_id = self.user.id
            comment.comment = self.POST['comment']
            comment.space_id = self.GET['space_id']
            comment.save()
            return HttpResponseRedirect('/space?id=' + self.GET['space_id'])

    @login_required(login_url='/signin')
    def like(self):
        tmp = SpaceRank.objects.filter(space_id=self.GET['space_id']).filter(user_id=self.user.id)
        if tmp.count() == 0:
            s = SpaceRank()
            s.space_id = self.GET['space_id']
            s.user_id = self.user.id
            s.rank = 1
            s.save()
        else:
            s = tmp[0]
            s.rank = 1
            s.save()
        return HttpResponseRedirect('/space?id=' + self.GET['space_id'])

    @login_required(login_url='/signin')
    def dislike(self):
        tmp = SpaceRank.objects.filter(space_id=self.GET['space_id']).filter(user_id=self.user.id)
        if tmp.count() == 0:
            s = SpaceRank()
            s.space_id = self.GET['space_id']
            s.user_id = self.user.id
            s.rank = -1
            s.save()
        else:
            s = tmp[0]
            s.rank = -1
            s.save()
        return HttpResponseRedirect('/space?id=' + self.GET['space_id'])

    @login_required(login_url='/signin')
    def profile(self):
        if self.method == 'POST':
            user = self.user
            user.availability = self.POST["availability"]
            user.wigu = self.POST["wigu"]
            user.education = self.POST["education"]
            user.language = self.POST["language"]
            user.about = self.POST["about"]
            user.interest = self.POST["interest"]
            user.civ = self.POST["civ"]
            user.cil = self.POST["cil"]
            user.save()
            return render(self, 'profile.html', {'user': user})
        else:
            pprint(self.user)
            pprint("---------------------")
            # return HttpResponse(self.user)
            # addresses = Spaces.objects.filter(user_id=self.user.id) #values_list('address', flat=True)
            return render(self, 'profile.html', {'user': self.user})

    @login_required(login_url='/signin')
    def delete_item(self):
        t = Spaces.objects.filter(id=self.GET["id"]).delete()
        return redirect('/panel')

    @login_required(login_url='/signin')
    def submit_item(self):
        # pprint(self.user.username)
        # self.user.username = "test11"
        # self.user.save()

        # s = Spaces()
        # s.address = "address1"
        # s.price = 4236
        # s.user_id = self.user.id
        # s.save()
        #
        # s = Spaces()
        # s.address = "address2"
        # s.price = 4695
        # s.user_id = self.user.id
        # s.save()
        #
        # s = Spaces()
        # s.address = "address3"
        # s.price = 4125
        # s.user_id = self.user.id
        # s.save()
        #
        s = Spaces()
        s.address = self.POST["address"]
        s.price = self.POST["price"]
        s.user_id = self.user.id
        s.save()
        # r = Spaces.objects.filter(user_id=self.user.id).values_list('address', flat=True)
        # pprint(r[0])
        return redirect('/panel')