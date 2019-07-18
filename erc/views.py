from django.http import Http404
from django.shortcuts import render
from .models import *
# Create your views here.
def home_view (request, *args, **kwargs):
	team=Team.objects.get(id=1)
	content={
		'team':team,
	}
	return render(request,"erc/index.html",content)

def event_detail(request,Event_id):
	try:
		event=Event.objects.get(pk=Event_id)
	except Event.DoesNotExist:
		raise Http404("Event Does Not Exist")
	return render(request,'erc/event_detail.html',{'event':event})