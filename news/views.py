from django.shortcuts import render
from news.models import News


def home(request):
    news = News.objects.all()
    return render(request, "home.html", context={"news": news})
