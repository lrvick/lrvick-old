from django.db import models
from tagging.fields import TagField

class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=250)
    path = models.SlugField()
    project_url = models.URLField('Project URL', blank=True)
    image = models.ImageField(upload_to='Image', blank=True)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    tags = TagField(blank=True)
    completion_date = models.DateField()
    draft = models.BooleanField('Safe as draft',default=False)
    class Meta:
        ordering = ['-completion_date']
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/projects/%s/" % self.path
