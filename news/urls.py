from news.views import home, news_details, category_form, news_form
from news.views import CategoryViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)


urlpatterns = [
  path("", home, name="home-page"),
  path('news/<int:id>', news_details, name='news-details-page'),
  path("categories/", category_form, name="categories-form"),
  path("news/", news_form, name="news-form"),
  path("api/", include(router.urls)),
]
