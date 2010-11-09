from django.db import models
from tagging.fields import TagField

class CodeSample(models.Model):
    title = models.CharField(max_length=250)
    path = models.SlugField()
    source_url = models.URLField('Code URL', blank=True)
    demo_url = models.URLField('Demo URL', blank=True)
    description = models.TextField(blank=True)
    tags = TagField(blank=True)
    draft = models.BooleanField('Safe as draft',default=False)
    class Meta:
        ordering = ['-title']
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/projects/%s/" % self.path
