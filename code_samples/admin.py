from django.contrib import admin
from code_samples.models import CodeSample
from django.db import models

class CodeSampleAdmin(admin.ModelAdmin):
	list_display = ('title', 'source_url','demo_url')
	search_fields = ('title', 'tags','description')
	prepopulated_fields = {"path": ("title",)}

admin.site.register(CodeSample, CodeSampleAdmin)
