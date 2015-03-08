from django.db import models

# Create your models here.
class WeatherNotifications(models.Model):
	name = models.CharField(verbose_name=u'Name', max_length=200)
	email = models.EmailField(verbose_name=u'Email', null=True, blank=True)
	location = models.CharField(verbose_name=u'Name', max_length=200)

	def __unicode__(self):
		return self.name