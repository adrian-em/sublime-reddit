from django.conf import settings
from django.shortcuts import render_to_response
import requests


def main_page(request):

    """
    Index page
    """
    w = requests.get("http://www.reddit.com/.json")
    c = w.json
    print c
    return render_to_response("sublime/index.html", {'c': c,
        'app_name': settings.APPLICATION_NAME, 'name': 'home'})


def comments_page(request, r, subreddit, comments, name, title):

    """
    Load comments
    """
    url = "http://www.reddit.com/r/" + subreddit + "/comments/" \
        + name + "/" + title + "/.json"
    print url
    w = requests.get(url)
    c = w.json
    return render_to_response("sublime/comments.html", {'c': c,
        'app_name': settings.APPLICATION_NAME, 'name': title})


def user_page(request, useruri):
    pass


def subreddit_page(request, subreddituri):

    """
    Load specific subreddit
    """
    url = "http://www.reddit.com/r/" + subreddituri + "/.json"
    print url
    w = requests.get(url)
    c = w.json
    return render_to_response("sublime/index.html", {'c': c,
        'app_name': settings.APPLICATION_NAME, 'name': subreddituri})


def reddit_next_page(request, after):

    """
    Load next page
    """
    url = "http://www.reddit.com/.json?after=" + after
    print url
    w = requests.get(url)
    c = w.json
    return render_to_response("sublime/index.html", {'c': c,
        'app_name': settings.APPLICATION_NAME, 'name': after})


def settings_page(request):

    """
    Info about app
    """
    return render_to_response("sublime/settings.html",
        {'app_name': settings.APPLICATION_NAME})
