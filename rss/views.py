from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from operator import itemgetter
from datetime import datetime
import feedparser
from htmlmin.decorators import minified_response

@minified_response
def index(request):
    if request.GET.get("url"):
        url = request.GET["url"]
        feed = feedparser.parse(url)
        request.session['url'] = url
        for entry in feed.entries:
            if "published" in entry:
                entry['published'] = entry['published'][:25]
            else:
                continue
    else:
        feed = None
    return render(request, 'rss/feeds.html', { 'feed' : feed, })

@minified_response
def sort_a(request):
    url = request.session['url']
    feed = feedparser.parse(url)
    tempEntries = feed['entries']
    for entry in feed.entries:
            if "published" in entry:
                entry['published'] = entry['published'][:25]
            else:
                continue
    try:
        tempEntries = sorted(tempEntries, key=itemgetter('published_parsed'))
    except:
        print("Cannot be sorted")
    feed['entries'] = tempEntries
    return render(request, 'rss/feeds.html', { 'feed' : feed, })

@minified_response
def sort_d(request):
    url = request.session['url']
    feed = feedparser.parse(url)
    tempEntries = feed['entries']
    for entry in feed.entries:
            if "published" in entry:
                entry['published'] = entry['published'][:25]
            else:
                continue
    try:
        tempEntries = sorted(tempEntries, key=itemgetter('published_parsed'), reverse=True)
    except:
        print("Cannot be sorted")
    feed['entries'] = tempEntries
    return render(request, 'rss/feeds.html', { 'feed' : feed, })

