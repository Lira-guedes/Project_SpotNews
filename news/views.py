from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category, User
from news.forms import CategoryForm, NewsForm
from news.serializers import CategorySerializer
from rest_framework import viewsets


def home(request):
    news = News.objects.all()
    return render(request, "home.html", context={"news": news})


def news_details(request, id):
    return render(request, 'news_details.html',
                  context={'news': get_object_or_404(News, pk=id)})


def category_form(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('home-page')
    return render(request, 'categories_form.html', {'form': form})


def news_form(request):
    form = NewsForm()
    categories = Category.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = News.objects.create(
                title=form.cleaned_data['title'],
                created_at=form.cleaned_data['created_at'],
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                author=form.cleaned_data['author'],
            )
            news.categories.set(form.cleaned_data['categories'])
            news.save()
            return redirect("home-page")
    return render(request, "news_form.html",
                  {"form": form, "categories": categories, "users": users})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
