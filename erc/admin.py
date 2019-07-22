from django.contrib import admin
from .models import Event, Blog, BlogPart, Team,Newsletter,News, reviews

# Register your models here.

admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(BlogPart)
admin.site.register(Team)
admin.site.register(Newsletter)
admin.site.register(News)
admin.site.register(reviews)