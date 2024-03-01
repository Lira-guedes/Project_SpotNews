from news.views import home, news_details, category_form, news_form
from django.urls import path

urlpatterns = [
  path("", home, name="home-page"),
  path('news/<int:id>', news_details, name='news-details-page'),
  path("categories/", category_form, name="categories-form"),
  path("news/", news_form, name="news-form")
]
