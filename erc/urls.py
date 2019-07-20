from django.contrib import admin
from django.urls import include,path
<<<<<<< HEAD
from .views import *
=======
<<<<<<< HEAD
from .views import home_view,event_detail,blog_view,newsletter_detail,news
=======
from .views import *
>>>>>>> b89beb28e8e751275e87642ed33b5a8f373c7c33
>>>>>>> cb44131719c403c89689bac7492c82d7aa2466d2
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
    path('newsletter/<int:Newsletter_id>/', newsletter_detail, name='newsletter_detail'),
    path('news/',news,name='news'),

]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
