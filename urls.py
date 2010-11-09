from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.syndication.feeds import Feed
from blog.models import Entry
from projects.models import Project
from code_samples.models import CodeSample
from blog.views import blog_index, blog_entry
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.views.generic.simple import direct_to_template
admin.autodiscover()

blog_dict = {
		    'queryset': Entry.objects.all(),
				'date_field': 'date',
}

sitemaps = {
		        'flatpages': FlatPageSitemap,
				    'blog': GenericSitemap(blog_dict, priority=0.6),
}

class BlogEntries(Feed):
	title = "Lance Vick's blog"
	description = "Documentation of the random adventures of Lance Vick."
	link = "/"
	feed_type = Rss201rev2Feed
	def items(self):
		return Entry.objects.order_by('-date')[:5]
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return item.body
	def item_pubdate(self, item):
		return item.date

feeds = {
		    'blog.xml': BlogEntries,
}
projects_dict = {
		    'queryset': Project.objects.all(),
}
code_dict = {
		    'queryset': CodeSample.objects.all(),
}
urlpatterns = patterns('',
		url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
		url(r'^adminfiles/', include('adminfiles.urls')),
		url(r'^markitup/', include('markitup.urls')),
		url(r'^admin/', include(admin.site.urls)),
		url(r'^comments/', include('django.contrib.comments.urls')),
		url(r'^feeds/(?P<url>.*)$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
#	  (r'^grappelli/', include('grappelli.urls')),
		url(r'^page/(?P<page>.*)/$', blog_index, name="pagination"),
		url(r'^tag/(?P<tag>.*)/page/(?P<page>.*)/$', blog_index, name="pagination-tag"),
		url(r'^tag/(?P<tag>.*)/$', blog_index, name="tag"),
	  url(r'^projects$', 'django.views.generic.list_detail.object_list' , dict(projects_dict, template_name='project_index.html')),
	  url(r'^code$', 'django.views.generic.list_detail.object_list' , dict(code_dict, template_name='code_index.html')),
		url(r'^$', blog_index, name="blog-index"),
		url(r'^(.*)/$', blog_entry, name="blog-entry"),
)
