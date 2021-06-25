from django import forms
from .models import Violation
from .models import Car

class requestForm(forms.ModelForm):
    class Meta:
        model = Violation
        fields = ('car','violation_type','longitude','latitude','comments','street',)

    car = forms.ModelChoiceField(queryset=Car.objects.all())
    violation_type = forms.CharField()
    longitude = forms.CharField()
    latitude = forms.CharField()
    street = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea)