import django_filters
from django import forms
from django_filters import DateFilter
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ViolationFilter(django_filters.FilterSet):
    class Meta:
        model = Violation
        fields = [
            'car',
            'violation_type',
            ]

    date_from = DateFilter(
        field_name='time_stamp',
        label="From",
        lookup_expr='gte',
        widget=DateInput
        )
    date_to = DateFilter(
        field_name='time_stamp',
        label="To",
        lookup_expr='lte',
        widget=DateInput
        )


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = [
            'car_id',
            'car_type',
            'num_passengers',
            'car_owner',
            'plate_num'
            ]

    car_id = django_filters.ModelChoiceFilter(
        queryset=Car.objects.all().values_list('car_id',
        flat=True)
        )
    plate_num = django_filters.CharFilter(
        field_name='plate_num',
        label="Plate Number",
        lookup_expr='icontains'
        )
    car_owner = django_filters.CharFilter(
        field_name='car_owner',
        label="Car Owner",
        lookup_expr='icontains'
        )
