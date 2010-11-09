from django.http import HttpResponse
from django.template import loader, Context
from django.http import Http404
from blog.models import Entry
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from tagging.models import Tag,TaggedItem

def blog_index(request, page=None, tag=None):
  page = page if page else 1
  if tag:
    tagged_objects = Tag.objects.get(name=tag)
    queryset = TaggedItem.objects.get_by_model(Entry, tagged_objects).order_by('-date').filter(draft=False)
  else:
		queryset = Entry.objects.order_by('-date').filter(draft=False)
  paginator = Paginator(queryset, 7)
  try:
    entries = paginator.page(page)
  except (EmptyPage, InvalidPage):
    entries = paginator.page(paginator.num_pages)
  return render_to_response('blog_index.html', {
		'entries': entries,
		'tag': tag,
		'page': int(page),
	}, context_instance=RequestContext(request))



def blog_entry(request, path):
	entry = get_object_or_404(Entry, path=path)
	return render_to_response('blog_entry.html', {
		'entry': entry
	}, context_instance=RequestContext(request))
