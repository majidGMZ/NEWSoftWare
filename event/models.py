from django.db import models
from django.utils import timezone
from django.urls import reverse
from .extensions.utils import jalali_converter
from account.models import Account
from django.contrib.auth import get_user_model
Account= get_user_model()
from django import template
register= template.Library()



# Create your models here.

class Events(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='event_user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    city = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    date_from = models.DateField(default=timezone.now)
    clock_from = models.TimeField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    clock_to = models.TimeField(default=timezone.now)
    members= models.ManyToManyField(Account,through='MemberEvent')

    def __str__(self):
        return self.title

    # bad az  ajnam shodan add be koja bere
    def get_absolute_url(self):
        return reverse("event:detail", kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def jdate_to(self):
        return jalali_converter(self.date_to)

    def jdate_from(self):
        return jalali_converter(self.date_from)


class Comment(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='comments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='username_comment')
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.text


class Discussion(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='discussion_account')
    city = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.city

    # bad az  ajnam shodan add be koja bere
    def get_absolute_url(self):
        return reverse("event:discussion_detail", kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def jdate_to(self):
        return jalali_converter(self.date_to)

    def jdate_from(self):
        return jalali_converter(self.date_from)


class CommentDiscussion(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='comments_discussion')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments_discussion_account')
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def __str__(self):
        return self.text


######member

class MemberEvent(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='member_event')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='spa_event')

    def __str__(self):
        return  self.account.username
    class Meta:
         unique_together= ('event','account')