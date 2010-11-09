from django.contrib import admin
from adminfiles.admin import FilePickerAdmin
from blog.models import Entry
from markitup.widgets import AdminMarkItUpWidget
from django.db import models

class EntryAdmin(FilePickerAdmin):
	list_display = ('title', 'date', 'draft')
	search_fields = ('title', 'body', 'tags')
	prepopulated_fields = {"path": ("title",)}
	adminfiles_fields = ('body',)

admin.site.register(Entry, EntryAdmin)

