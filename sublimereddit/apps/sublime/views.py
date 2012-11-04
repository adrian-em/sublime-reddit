from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
import requests


def main_page(request):

    w = requests.get("http://www.reddit.com/.json")
    c = w.json
    print c
    return render_to_response("sublime/index.html", {'c': c, 'app_name': settings.APPLICATION_NAME, 'name': 'home'})


def comments_page(request, commentsuri):
    pass


def user_page(request, useruri):
    pass


def subreddit_page(request, subreddituri):
    url = "http://www.reddit.com/r/" + subreddituri + "/.json"
    print url
    w = requests.get(url)
    c = w.json
    return render_to_response("sublime/index.html", {'c': c, 'app_name': settings.APPLICATION_NAME, 'name': subreddituri})


def reddit_next_page(request, after):
    url = "http://www.reddit.com/.json?after=" + after
    print url
    w = requests.get(url)
    c = w.json
    return render_to_response("sublime/index.html", {'c': c, 'app_name': settings.APPLICATION_NAME, 'name': after})
