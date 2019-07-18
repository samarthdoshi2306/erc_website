from django.http import Http404
from django.shortcuts import render
from .models import *
from django.db import connections

# Create your views here.
def home_view (request, *args, **kwargs):
	anirudh=Team.objects.get(id=2)
	jian=Team.objects.get(id=3)
	queryset=Team.objects.all()

	return render(request,"erc/index.html",{'anirudh':anirudh,'jian':jian,'team':queryset })

def event_detail(request,Event_id):
	try:
		event=Event.objects.get(pk=Event_id)
	except Event.DoesNotExist:
		raise Http404("Event Does Not Exist")
	return render(request,'erc/event_detail.html',{'event':event})