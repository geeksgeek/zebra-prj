# blog/models.py

from django.core.urlresolvers import reverse
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(unique=True, allow_unicode=True, help_text='one word for title alias.')
	description = models.CharField(max_length=100, blank=True, help_text='simple description text.')
	content = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-modify_date']

	def __str__(str):
		return self.title

	def get_albsolute_url(self):
		return reverse('blog:post_detail', args=[self.slug])

	def get_previous_post(self):
		return self.get_previous_by_modify_date()

	def get_next_post(self):
		return self.get_next_by_modify_date()

	
