from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CategoryForm

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