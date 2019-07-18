from django.http import Http404
from django.shortcuts import render
from erc.models import Event
# Create your views here.
def home_view (request, *args, **kwargs):
	return render(request,"erc/index.html",{})

def event_detail(request,Event_id):
	try:
		event=Event.objects.get(pk=Event_id)
	except Event.DoesNotExist:
		raise Http404("Event Does Not Exist")
	return render(request,'erc/event_detail.html',{'event':event})