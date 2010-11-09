import time,feedparser,re
from datetime import datetime
from django.utils.encoding import smart_unicode
from django import template

register = template.Library()

def twitter(user, limit):
    twitter_feed = feedparser.parse("http://twitter.com/statuses/user_timeline/"+user+".rss")
    data_list = []
    for entry in twitter_feed['entries'][:limit]:
        time = entry.updated_parsed
        published = datetime(time.tm_year, time.tm_mon, time.tm_mday, time.tm_hour, time.tm_min, time.tm_sec)
        link = entry.links[0].href
        text = re.sub(r'^\w+:\s', '', entry['title'])
        data_list.append([published, link, text])
    if data_list:
        return  { 'tweets': data_list }
    else: return ""
register.inclusion_tag('includes/twitter.html')(twitter)
