from django.db import models
from django.contrib.admin.models import User
from tagging.fields import TagField
from datetime import datetime
from markitup.fields import MarkupField

class Entry(models.Model):
	title = models.CharField('Title', max_length=255)
	path = models.SlugField('Path', max_length=255)
	date = models.DateTimeField('Published on', default=datetime.now)
	image = models.ImageField(upload_to='Image', blank=True)
	description = models.CharField('Description', max_length=255, blank=True)
	body = MarkupField()
	tags = TagField(blank=True)
	commenting = models.BooleanField('Allow Commenting',default=True)
	draft = models.BooleanField('Safe as draft',default=False)
	class Meta:
			verbose_name_plural = "Entries"
	@models.permalink
	def get_absolute_url(self):
		return ('blog-entry', (self.path,), {})
	def __unicode__(self):
		return self.title
