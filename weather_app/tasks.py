from __future__ import absolute_import

# database
from .models import *

# email importings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.conf import settings

from weather_project.celery import app
from celery.task import task
from celery.decorators import periodic_task
from time import sleep
import urllib, json
import datetime


@app.task
def add(x, y):
    return x + y


# get weather json
def get_weather(each_location):
	url = "http://api.openweathermap.org/data/2.5/weather?q=" + each_location
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	return data

# # get email and location from database
# weather_notification = WeatherNotifications.objects.all()
# for weather_owner in weather_notification:
# 	name = weather_owner.name
# 	email = weather_owner.email
# 	location = weather_owner.location


# @app.task
@periodic_task(run_every=datetime.timedelta(hours=24))
def send_welcome_mail():
	# get email and location from database
	weather_notification = WeatherNotifications.objects.all()
	for weather_owner in weather_notification:
		name = weather_owner.name
		email = weather_owner.email
		location = weather_owner.location

		# get weather json
		weather_json = get_weather(location)

		country = weather_json['sys']['country']
		description = weather_json['weather'][0]['description']
		temp = weather_json['main']['temp']
		pressure = weather_json['main']['pressure']
		# sea_level = weather_json['main']['sea_level']
		humidity = weather_json['main']['humidity']
		wind_speed = weather_json['wind']['speed']

		subject = "Weather Report"
		html_content = render_to_string('weather_report.html', { 'name': name, 
	                                                   'country': country,
	                                                    'description': description,
	                                                    'temp': temp,
	                                                    'pressure': pressure,
	                                                    # 'sea_level': sea_level,
	                                                    'humidity': humidity,
	                                                    'wind_speed': wind_speed, })
		text_content = strip_tags(html_content)
	                       
		msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, to=[email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		# return True


# @app.task
# def send_welcome_mail(appuser):
# 	subject = "Weather Report"
# 	html_content = render_to_string('registration/email/welcome.html', { 'site_url': settings.SITE_URL, 
#                                                    'verification_key': appuser.verification_key,
#                                                     'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS })
# 	text_content = strip_tags(html_content)
                       
# 	msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_TO, to=[appuser.email])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send()
# 	return True



# @app.task
# def mul(x, y):
#     return x * y


# @app.task
# def xsum(numbers):
#     return sum(numbers)