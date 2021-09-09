from .models import product
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = product
        fields = ['cat', 'price',]
