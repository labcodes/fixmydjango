# coding: utf-8

from django.db.models import Q

import django_filters

from core.filters import AllValuesFilterWithEmpty
from .models import ErrorPost


class ErrorPostFilter(django_filters.FilterSet):
    exception_type = AllValuesFilterWithEmpty(empty_label="All types")
    search = django_filters.MethodFilter(action='filter_exception')

    class Meta:
        model = ErrorPost

    def filter_exception(self, queryset, value):
        return queryset.filter(
            Q(exception_type__icontains=value) |
            Q(error_message__icontains=value))