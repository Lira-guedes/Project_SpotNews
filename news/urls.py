from news.views import home, news_details
from django.urls import path

urlpatterns = [
  path("", home, name="home-page"),
  path('news/<int:id>', news_details, name='news-details-page'),
]
