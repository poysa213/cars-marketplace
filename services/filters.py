import django_filters

from .models import ServiceProvider


class ServiceFilter(django_filters.FilterSet):
    service = django_filters.CharFilter(field_name='services__name', lookup_expr='contains')

    class Meta:
        model = ServiceProvider
        fields = ['services']