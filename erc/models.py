from django.db import models

# Create your models here.

class Event(models.Model):
	name=models.CharField(max_length=80)
	content=models.TextField()
	date=models.DateTimeField()
	img=models.ImageField(upload_to=None, 
		height_field=None, 
		width_field=None, 
		max_length=100)

class BlogArticle(models.Model):
	title=models.CharField(max_length=80)
	content=models.TextField()
	# anonymous=models.BooleanField(default=False)
	# author=models.CharField(max_length=80,editable=True if anonymous==False else False,
	# 	default='Anonymous')
	author=models.CharField(max_length=80)
	date=models.DateTimeField()

class BlogPic(models.Model):
	img=img=models.ImageField(upload_to=None, 
		height_field=None, 
		width_field=None, 
		max_length=100)
	BlogTitle=models.CharField(max_length=80)