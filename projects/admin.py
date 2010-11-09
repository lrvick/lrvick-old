from django.contrib import admin
from projects.models import Project, Client
from django.db import models

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'completion_date')
	search_fields = ('title', 'completion_date', 'tags','description')
	prepopulated_fields = {"path": ("title",)}

class ClientAdmin(admin.ModelAdmin):
	list_display = ('name', 'url')
	search_fields = ('name', 'url')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)

#---------------- flatpages hacks -------------------------------
# still 'ModelFormMetaclass' object is not iterable did you touch and stuff?
#ah ok it took , as in no errors but ti still dos not allow dots
#and the rrror message still reads
# This value must contain only letters, numbers, underscores, dashes or slashes.

from django import forms
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin

class FlatpageForm(forms.ModelForm):
	url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$', 
	help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
	error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes or slashes. This is the error being called."))
	class Meta:
		model = FlatPage

class FlatPageAdmin(admin.ModelAdmin):
	form = FlatpageForm
	fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
	)
	list_display = ('url', 'title')
	list_filter = ('sites', 'enable_comments', 'registration_required')
	search_fields = ('url', 'title')

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
