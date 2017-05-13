from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=2000)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True,null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True,null=True)
	post = models.ForeignKey(Post)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.text
	
