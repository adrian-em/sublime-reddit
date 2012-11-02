from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import requests


def main_page(request):

    w = requests.get("http://www.reddit.com/.json")
    c = w.json
    print c
    return render_to_response("sublime/index.html", {'c': c, 'app_name': settings.APPLICATION_NAME})
