from django.shortcuts import render
from polls.models import Gps 
#from polls.models import Poll

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

def gps(request):
	user_name=request.GET['name']
	user_lat=request.GET['latitude']
	user_lon=request.GET['longitude']
	user_prof=Gps(name=user_name,latitude=user_lat,longitude=user_lon)
	user_prof.save()
	return HttpResponse("name %s" % user_name)
