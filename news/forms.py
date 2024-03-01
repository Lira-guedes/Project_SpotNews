from django import forms
from news.models import Category, User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CategoryForm(forms.ModelForm):
    class Meta:
      model = Category
      fields = "__all__"
      label= {
          "name": "Nome" 
      }
    # name = forms.CharField(max_length=200, required=True, label="Nome")


def title_validate(title):
    if len(title.split()) < 2:
        raise ValidationError(_("O título deve conter pelo menos 2 palavras."))


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        validators=[title_validate],
        required=True
    )
    author = forms.ModelChoiceField(required=True, queryset=User.objects.all())
    content = forms.CharField(required=True, widget=forms.Textarea)
    image = forms.ImageField(required=False)
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
      )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
      )
