from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.views import View
from .form import requestForm
from geopy.geocoders import Nominatim
import json
from django.http import JsonResponse


@login_required(login_url='/auth/login')
def index(request):
    cars = Car.objects.all()
    violations = Violation.objects.all()
    traffics = Traffic.objects.all()
    context = {
        'cars': cars,
        'viols': violations,
        'traffics': traffics,
    }
    return render(request=request, template_name='main/index.html', context=context)


def search_car(request):
    if request.method == 'POST':
        search_term = json.loads(request.body).get('term', '')
        search_res = Car.objects.filter(
                        car_id=search_term, owner=request.user) | Car.objects.filter(
                        car_type=search_term, owner=request.user) | Car.objects.filter(
                        car_owner__icontains=search_term, owner=request.user) | Car.objects.filter(
                        location__icontains=search_term, owner=request.user)
        data = search_res.values()
        return JsonResponse(list(data), safe=False)


@login_required(login_url='/auth/login')
def cars(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request=request, template_name='cars/cars.html', context=context)


@login_required(login_url='/auth/login')
def carDetail(request, car_id):
    carDetail = Car.objects.get(car_id=car_id)
    context = {'car': carDetail}
    return render(request=request, template_name='cars/car.html', context=context)


@login_required(login_url='/auth/login')
def carRegister(request):
    return render(request=request, template_name='cars/car-register.html')

@login_required(login_url='/auth/login')
def traffics(request):
    traffics = Traffic.objects.all()
    context = {'traffics': traffics}
    return render(request=request, template_name='traffics/traffics.html', context=context)


@login_required(login_url='/auth/login')
def violations(request):
    violations = Violation.objects.all()
    context = {'viols': violations}
    return render(request=request, template_name='viols/violations.html', context=context)


class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def getLocation(self):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(self.latitude+","+self.longitude)
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        code = address.get('country_code')
        zipcode = address.get('postcode')
        return city


class newViolation(View):
    def get(self, request):
        form = requestForm()
        context = {'form': form}
        return render(request=request, template_name='viols/new-violation.html', context=context)

    def post(self, request):
        form = requestForm(request.POST)
        if form.is_valid():
            form.save()
            # car = form.cleaned_data['car']
            car = form.cleaned_data['car']
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            street = form.cleaned_data['street']
            violation_type = form.cleaned_data['violation_type']
            comments = form.cleaned_data['comments']
        context = {
            'form': form,
            'car': car,
            'longitude': longitude,
            'latitude': latitude,
            'street': street,
            'violation_type': violation_type,
            'comments': comments,
        }
        return render(request=request, template_name='viols/new-violation.html', context=context)
