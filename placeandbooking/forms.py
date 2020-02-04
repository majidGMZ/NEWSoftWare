from django import forms
from. import models

class bookingmodel(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['Arrival','Depart']
