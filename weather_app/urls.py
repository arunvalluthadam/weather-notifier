from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'weather_app.views.home', name='home'),
    url(r'^success/$', 'weather_app.views.success', name='success'),
    url(r'^weather-report/$', 'weather_app.views.weather_report', name='weather_report'),
)