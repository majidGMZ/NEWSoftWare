from django.contrib import admin
from .models import Events, Comment, CommentDiscussion, Discussion,MemberEvent

admin.site.register(Events)
admin.site.register(Comment)
admin.site.register(CommentDiscussion)
admin.site.register(Discussion)
admin.site.register(MemberEvent)
