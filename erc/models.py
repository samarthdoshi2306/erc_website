from django.db import models
from django.urls import reverse
# Create your models here.
# POSTS=[('Convener','Convener'),
#          ('Volunteer','Volunteer'),
#          ('Manager','Manager')]

class Event(models.Model):
	name=models.CharField(max_length=80)
	problem_statement=models.FileField(upload_to='media/events/pdf',null=True,blank=True)
	video=models.CharField(max_length=100,null=True,blank=True)
	event_status=models.CharField(max_length=100,null=True,blank=True)
	content=models.TextField(null=True,blank=True)
	date=models.DateField(null=True,blank=True)
	img=models.ImageField(upload_to='media/events',max_length=100)
	filterClass=models.CharField(max_length=80,blank=True)
	def get_absolute_url(self):
		return reverse('erc:event_detail',kwargs={'Event_id':self.id})

class Team(models.Model):
	name=models.CharField(max_length=80,blank=False)
	#post = forms.ChoiceField(choices=POSTS, widget=forms.RadioSelect,blank=False)
	post=models.CharField(max_length=80)
	image=models.ImageField(upload_to='media/team',blank=True)
	fb=models.CharField(max_length=80,null=True,blank=True)
	linkedin=models.CharField(max_length=80,null=True,blank=True)
	github=models.CharField(max_length=80, null=True, blank=True)


class Blog(models.Model):
	title=models.CharField(max_length=80)
	parts=models.IntegerField()
	author=models.CharField(max_length=80)
	date=models.DateField()
	CATEGORY_CHOICES = (
    ("informative", ("informative")),
    ("tutorials", ("tutorials")),
    ("projects", ("projects"))
     )
	filterClass=models.CharField(max_length=80,choices=CATEGORY_CHOICES, default="informative")
	content=models.TextField(null=True,blank=True,default="Don't know")


	def get_absolute_url(self):
		return reverse('erc:blog',kwargs={'name':self.title})

class BlogPart(models.Model):
	Blogtitle=models.CharField(max_length=80,null=False)
	content=models.TextField(blank=True)
	partNum=models.IntegerField()
	img=models.ImageField(upload_to='media/blogs',
		height_field=None,
		width_field=None,
		max_length=100,
		blank=True)
	# def __str__(self):
	# 	return '%s'%self.img.url

class Newsletter(models.Model):
	title=models.CharField(max_length=100)
	image=models.ImageField(upload_to='media/newsletter')
	content=models.TextField(blank=True)

# class BlogPic(models.Model):
# 	img=models.ImageField(upload_to='media/blogs',
# 		height_field=None,
# 		width_field=None,
# 		max_length=100)
# 	BlogTitle=models.CharField(max_length=80,null=False)
# 	BlogPartNum=models.DecimalField(decimal_places=2,max_digits=2,null=False,default=False)

class News(models.Model):
	image=models.ImageField(upload_to='media/news')
	date=models.DateField()
	pdf=models.FileField(upload_to='media/news/pdfs')
	headline=models.CharField(max_length=80)

class reviews(models.Model):
	name=models.CharField(max_length=80)
	description=models.CharField(max_length=100)
	image=models.ImageField(upload_to='media/team')
	review=models.TextField()
