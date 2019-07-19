from django.contrib import admin
from django.urls import include,path
from .views import home_view,event_detail
from django.conf.urls.static import static
from django.conf import settings

app_name="erc"
urlpatterns = [
	#home page
    path('', home_view , name='home'),
    #events page
    path('events/<int:Event_id>/',event_detail, name='event_detail'),
    #blogs page

    #newsletter page


]#+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
