from django import forms
from .models import Violation
from .models import Car


CAR_TYPE = (
    ('Auto', 'Auto'),
    ('Truck', 'Truck'),
)


VIO_TYPE = (
    ('Speed', 'Speed'),
    ('Emergency Vehicle', 'Emergency Vehicle'),
    ('Tailgating', 'Tailgating'),
    ('Red Light', 'Red Light'),
    ('Carpool', 'Carpool'),
)


class requestForm(forms.ModelForm):
    class Meta:
        model = Violation
        fields = (
            'car',
            'violation_type',
            'longitude',
            'latitude',
            'comments',
            )

    car = forms.ModelChoiceField(queryset=Car.objects.all())
    violation_type = forms.CharField(widget=forms.Select(choices=VIO_TYPE))
    longitude = forms.CharField()
    latitude = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea)


class carForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'car_id',
            'car_type',
            'num_passengers',
            'car_owner',
            'plate_num',
            )

    car_id = forms.CharField()
    car_type = forms.CharField(widget=forms.Select(choices=CAR_TYPE))
    num_passengers = forms.CharField()
    car_owner = forms.CharField()
    plate_num = forms.CharField()
