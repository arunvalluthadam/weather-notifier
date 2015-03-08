from django import forms
from .models import *

class WeatherNotificationsForm(forms.ModelForm):
	class Meta:
		model = WeatherNotifications
		field = ('name', 'email', 'location')
		widgets = {
			'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"}),
			'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
			'location': forms.TextInput(attrs={"class": "form-control", "placeholder": "Location"}),
		}