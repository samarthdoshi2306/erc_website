from django.contrib import admin
from django.urls import include,path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name="erc"
urlpatterns = [
	#home page
    path('', home_view , name='home'),
    #testimonials page
    path('testimonials',reView, name='review'),
    #events page
    path('events/<int:Event_id>/',event_detail, name='event_detail'),
    #blogs page
    path('blog/<name>',blog_view, name='blog'),
    #blog list
    path('blog',blogList,name='blogList'),
    #newsletter page
        #path('newsletter/<int:Newsletter_id>/', newsletter_detail, name='newsletter_detail'),
    path('news/',news,name='news'),
    #create event
    #path('create_event/',create_event.as_view(),name='create_event'),
    #create newsletter
    #path('create_news/',create_news.as_view(),name='create_news'),

]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
