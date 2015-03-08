import urllib, json

def get_weather(each_location):
	url = "http://api.openweathermap.org/data/2.5/weather?q=" + each_location
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	return data
	# print data['weather']['description']


# url = "http://api.openweathermap.org/data/2.5/weather?q=thrissur"
# response = urllib.urlopen(url);
# data = json.loads(response.read())
# split = data["weather"]["description"]