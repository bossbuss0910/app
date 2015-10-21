from django.shortcuts import render_to_respons, get_object_or_404e
from django.template import Context, loader
from django.core.context_processors import csrf
from django.http import HttpResponse
# Create your views here.


#DB-Gps input
from gpss.models import Gps,Friend
def test(request):
	c = {}
        c.update(csrf(request))
	return render_to_response('topEV.html',c)

def post(request):
	bttnlist = Gps(u_id=request.POST["id"],name=request.POST["name"],latitude = request.POST["latitude"], longitude = request.POST["longitude"])
	bttnlist.save()
	return HttpResponse("success!!.")

def get(request,u_id):
	p = get_object_or_404(Friend, user1id=u_id)
	return render_to_response('response.htmli',{'friend':p})
