import requests
from django.shortcuts import render
from django.shortcuts import redirect

news_url = "https://www.reddit.com/r/programming/.json"


def index(request):
    if not request.user.is_authenticated:
        return redirect("https://ai.gov.ae/codershq")

    return redirect("events:all")


def landing(request):
    return render(request, "pages/welcome.html")


def news(request):
    resp = requests.get(url=news_url, headers={"User-agent": "your bot 0.1"})
    body = resp.json()
    context = {"body": body["data"]["children"]}
    return render(request, "dashboard/news.html", context)