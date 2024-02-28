from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    role = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


def content_validate(content):
    if content.strip() == "":
        raise ValidationError(_("Este campo não pode estar vazio."))


def title_validate(title):
    if len(title.split()) < 2:
        raise ValidationError(_("O título deve conter pelo menos 2 palavras."))


class News(models.Model):
    content = models.TextField(
        null=False, blank=False, validators=[content_validate]
      )
    title = models.CharField(
        null=False, blank=False, validators=[title_validate], max_length=200
      )
    created_at = models.DateField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    categories = models.ManyToManyField(Category, related_name="news")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
      )

    def __str__(self):
        return self.title
