import django_filters
from django_filters import CharFilter, DateFilter
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains')
    content = CharFilter(field_name="content", lookup_expr='icontains')
    start_date = DateFilter(field_name="date_posted", lookup_expr='gte')
    end_date = DateFilter(field_name="date_posted", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['title', 'content']
