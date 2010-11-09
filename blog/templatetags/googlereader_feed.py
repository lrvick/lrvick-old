import time,feedparser,re
from datetime import datetime
from django.utils.encoding import smart_unicode
from django import template

register = template.Library()

def googlereader(user, limit):
    googlereader_feed = feedparser.parse("http://www.google.com/reader/public/atom/user/"+user+"/state/com.google/broadcast")
    data_list = []
    for entry in googlereader_feed['entries'][:limit]:
        time = entry.updated_parsed
        title = entry.title
        published = datetime(time.tm_year, time.tm_mon, time.tm_mday, time.tm_hour, time.tm_min, time.tm_sec)
        link = entry.links[0].href
        text = re.sub(r'^\w+:\s', '', entry['title'])
        data_list.append([published, link, text])
    if data_list:
        return  { 'items': data_list }
    else: return ""
register.inclusion_tag('includes/googlereader.html')(googlereader)
