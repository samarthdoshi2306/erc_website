from django.contrib import admin
from .models import Event,BlogArticle,BlogPic
# Register your models here.

admin.site.register(Event)
admin.site.register(BlogArticle)
admin.site.register(BlogPic)