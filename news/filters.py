from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from .models import Post, User


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author__user',
        queryset=User.objects.all(),
        label='Author',
    )
    time_in = DateFilter(lookup_expr='lt', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
