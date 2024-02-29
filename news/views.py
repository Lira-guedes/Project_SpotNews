from django.shortcuts import render, get_object_or_404
from news.models import News


def home(request):
    news = News.objects.all()
    return render(request, "home.html", context={"news": news})


def news_details(request, id):
    return render(request, 'news_details.html',
                  context={'news': get_object_or_404(News, pk=id)})
