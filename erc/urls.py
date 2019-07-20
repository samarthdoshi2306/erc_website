from django.contrib import admin
from django.urls import include,path
from .views import home_view,event_detail,blog_view,newsletter_detail
from django.conf.urls.static import static
from django.conf import settings

app_name="erc"
urlpatterns = [
	#home page
    path('', home_view , name='home'),
    #events page
    path('events/<int:Event_id>/',event_detail, name='event_detail'),
    #blogs page
    path('blog',blog_view, name='blogs'),
    #newsletter page
    path('newsletter/<int:Newsletter_id>/', newsletter_detail, name='newsletter_detail')

]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
