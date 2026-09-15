import django_filters
from django import forms
from .models import Task

class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        method='filter_self',
        widget=forms.CheckboxInput,
        label='Только свои задачи',
        required=False,
    )

    def filter_self(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']