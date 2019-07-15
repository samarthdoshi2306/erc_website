from django.contrib import admin
from .models import Event, Blog, BlogPart, BlogPic

# Register your models here.

admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(BlogPart)
admin.site.register(BlogPic)