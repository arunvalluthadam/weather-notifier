from django.contrib import admin
from .models import *

# Register your models here.
class WeatherNotificationsAdmin(admin.ModelAdmin):
	model = WeatherNotifications
	list_display = ('name','email','location')
	search_fields = ['name']

admin.site.register(WeatherNotifications, WeatherNotificationsAdmin)