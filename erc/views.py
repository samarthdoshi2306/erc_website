from django.http import Http404
import django.views.generic as generic_views
from django.shortcuts import render
from .models import *
from .forms import *
from django.db import connections

# Create your views here.
def home_view (request, *args, **kwargs):
	team=Team.objects.all()
	event=Event.objects.all()
	news=Newsletter.objects.all()
	content={
	'team':team,
	'events':event,
	'news':news,
	}
	return render(request,"erc/index.html",content)


def event_detail(request,Event_id):
	try:
		event=Event.objects.get(pk=Event_id)
	except Event.DoesNotExist:
		raise Http404("Event Does Not Exist")
	return render(request,'erc/event_detail.html',{'event':event})

def blogList(request,*args,**kwargs):
	queryset=Blog.objects.all()
	content={
	'blogs':queryset,
	}
	return render(request,'erc/blog/blogList.html',content)

def blog_view(request,name, *args, **kwargs):
	try:
		blog = BlogPart.objects.filter(
		Blogtitle = '{}'.format(name)).order_by('partNum').values_list('img')
	except Exception as e:
		return Http404("Sorry, we couldn't find what you're looking for :(")

	images = list(blog)
	img=[]
	for image in images:
		img.append(image[0])
	content={
	'blog' :img,
	}
	#search for the html file named 'name'
	return render(request,"erc/blog/{}.html".format(name),content)

def reView(request,*args, **kwargs):
	revs=reviews.objects.all()
	return render(request,'erc/reviews/testimonials.html',{'revs':revs})

# def newsletter_detail(request,Newsletter_id):
# 	try:
# 		newsletter=Newsletter.objects.get(pk=Newsletter_id)
# 	except Newsletter.DoesNotExist:
# 		raise Http404("Newsletter Does Not Exist")
# 	return render(request,'erc/newsletter_detail.html',{'newsletter':newsletter})

def news(request):
	news=News.objects.all().order_by('-id')
	return render(request,'erc/news.html',{'news':news})

class create_event(generic_views.CreateView):
	queryset=Event.objects.all()
	template_name='erc/create_event.html'
	form_class=EventForm

class create_news(generic_views.CreateView):
	queryset=News.objects.all()
	template_name='erc/create_news.html'
	form_class=NewsForm