from django.db import models

# Create your models here.

class Event(models.Model):
	name=models.CharField(max_length=80)
	problem_statement=models.FileField(null=True,blank=True)
	video=models.CharField(max_length=100,null=True,blank=True)
	event_status=models.CharField(max_length=100,null=True,blank=True)
	content=models.TextField(null=True,blank=True)
	date=models.DateField(null=True,blank=True)
	img=models.ImageField(max_length=100)

class Blog(models.Model):
	title=models.CharField(max_length=80)
	parts=models.DecimalField(decimal_places=2,max_digits=2)
	author=models.CharField(max_length=80)
	date=models.DateTimeField()

class BlogPart(models.Model):
	Blogtitle=models.CharField(max_length=80,null=False)
	content=models.TextField(null=False)
	partNum=models.DecimalField(decimal_places=2,max_digits=2,null=False)


class BlogPic(models.Model):
	img=img=models.ImageField(upload_to=None,
		height_field=None,
		width_field=None,
		max_length=100)
	BlogTitle=models.CharField(max_length=80,null=False)
	BlogPartNum=models.DecimalField(decimal_places=2,max_digits=2,null=False,default=False)