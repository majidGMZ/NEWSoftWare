from django.shortcuts import render
from account.models import Spaces
from account.models import SpaceRank
from account.models import Comments
from django.db.models import Sum


class Front:
    def SpacesList(self):
        spaces = Spaces.objects.all()
        return render(self, 'account/Spaces.html', {'spaces': spaces})



    def Space(self):
        space = Spaces.objects.filter(id=self.GET['id'])
        comments = Comments.objects.filter(space_id=self.GET['id'])
        rank = SpaceRank.objects.filter(space_id=self.GET['id']).aggregate(Sum('rank'))
        mrank = rank['rank__sum']
        if mrank is None:
            mrank = 0
        return render(self, 'account/SingleSpace.html', {'space': space[0], 'comments': comments, 'rank': mrank})

