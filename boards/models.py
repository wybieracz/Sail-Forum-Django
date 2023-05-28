from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdown import markdown
from django.utils.html import mark_safe
from misc.markdown_extension import EscapeHTML
from django.conf import settings

# Create your models here.

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True, verbose_name='Nazwa')
	description = models.CharField(max_length=50, verbose_name='Opis')
	creation_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'kategorię'
		verbose_name_plural = 'kategorie'

class Topic(models.Model):
	subject = models.CharField(max_length=255, unique=True)
	board = models.ForeignKey(Board, on_delete=models.SET_NULL, related_name='topics', null=True)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='topics', null=True)
	created_on = models.DateTimeField(auto_now_add=True)	
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.subject

	def get_last_posts_pageno(self):
		rem = self.posts.count() % settings.POST_PAGINATE_BY
		quo = self.posts.count() // settings.POST_PAGINATE_BY
		if rem == 0:
			pageno = quo
		else:
			pageno = quo + 1
		return pageno

	def get_pageno_of_post(self,post):
		queryset = self.posts.all().order_by('id')
		post_index = None
		for index,value in enumerate(queryset, start=1):
			if value.id == post.id:
				post_index = index 
				break
		#get page location
		rem = post_index % settings.POST_PAGINATE_BY
		quo = post_index // settings.POST_PAGINATE_BY
		if rem == 0:
			pageno = quo
		else:
			pageno = quo + 1
		return pageno

class Post(models.Model):
	message = models.CharField(max_length=5000)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, related_name='posts', null=True)
	updated_on = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return first 30 characters of message only
		return (self.message[:30] if len(self.message)>30 else self.message)

	def get_message_as_markdown(self):
		return mark_safe(markdown(self.message, extensions=[EscapeHTML()]))