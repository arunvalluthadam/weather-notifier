from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context
from django.views.decorators.csrf import csrf_exempt
from .forms import *

# ---------------------- Email Imports -------------------------------------
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


# ---------------------- past Email Imports -------------------------------------
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# from django.core.mail import EmailMessage
# from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings
# ---------------------- End Email Imports -------------------------------------

# Create your views here.
@csrf_exempt
def home(request):
	if request.method == "POST":
		form = WeatherNotificationsForm(request.POST)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.save()
			# -------------------------------------------- send email ------------------
			subject = "Thank you For Supporting me!!!"
			message = "You will get peroidic weather information soon..."
			from_email = settings.EMAIL_HOST_USER
			to_list = [save_it.email]
			send_mail(subject, message, from_email, to_list, fail_silently=False)
			# -------------------------------------------- end send email ------------------
			return HttpResponseRedirect('/success')
		else:
			print form.errors
	else:
		form = WeatherNotificationsForm()
	variables = RequestContext(request, {
		'form':form,
	})
	return render_to_response('index.html', variables)

def success(request):
	# ---------------------------------------------------------------------
    # subject = "Weather Report"
    # html_content = render_to_string('weather_report.html')
    # text_content = strip_tags(html_content)

    # msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, to=['arunvalluthadam@gmail.com'])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    # # if msg.send():
    # # 	return True
    return render_to_response('success.html')

def weather_report(request):
	return render_to_response('weather_report.html')