from django.shortcuts import render
from django.db.models import Count
from .models import *
from django.contrib.auth.decorators import login_required
from django.views import View
from .form import requestForm, carForm
from .filters import *
import geocoder


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
    return render(
        request=request,
        template_name='main/index.html',
        context=context
        )


def count_viols(car):
    return Violation.objects.filter(car=car).count()


def getLocation(lat, lng):
    key = 'AvDna5jFe4i0lOa_SFLUGDrPufWLGEvdLVrgC1P3TVdPGbU3vbSb9AfpCDaYg7DK'
    location = geocoder.bing(
                            [lat, lng],
                            method='reverse',
                            key=key)

    country = location.country
    state = location.state
    city = location.city
    street = location.street
    postal = location.postal
    ret = [str(street), str(state)]

    return ", ".join(ret)


@login_required(login_url='/auth/login')
def cars(request):
    cars = Car.objects.all()
    viols = [count_viols(car) for car in cars]
    all_recs = zip(cars, viols)
    filters = CarFilter(request.GET, queryset=cars)
    cars = filters.qs
    viols = [count_viols(car) for car in cars]
    all_recs = zip(cars, viols)
    context = {
        'all_recs': all_recs,
        'filters': filters,
        }

    return render(
        request=request,
        template_name='cars/cars.html',
        context=context
        )


@login_required(login_url='/auth/login')
def carDetail(request, car_id):
    carDetail = Car.objects.get(car_id=car_id)
    context = {
        'car': carDetail,
        }

    return render(
        request=request,
        template_name='cars/car.html',
        context=context
        )


@login_required(login_url='/auth/login')
def carRegister(request):
    return render(
        request=request,
        template_name='cars/car-register.html'
        )

@login_required(login_url='/auth/login')
def traffics(request):
    traffics = Traffic.objects.all()
    context = {
        'traffics': traffics,
        }

    return render(
        request=request,
        template_name='traffics/traffics.html',
        context=context
        )


@login_required(login_url='/auth/login')
def violations(request):
    violations = Violation.objects.all()
    streets = [getLocation(violation.latitude, violation.longitude) for violation in violations]
    all_recs = zip(violations, streets)
    filters = ViolationFilter(request.GET, queryset=violations)
    violations = filters.qs
    streets = [getLocation(violation.latitude, violation.longitude) for violation in violations]
    all_recs = zip(violations, streets)
    context = {
        'all_recs': all_recs,
        'filters': filters
        }

    return render(
        request=request,
        template_name='viols/violations.html',
        context=context
        )


class newViolation(View):
    def get(self, request):
        form = requestForm()
        context = {
            'form': form,
            }
        return render(
            request=request,
            template_name='viols/new-violation.html',
            context=context
            )

    def post(self, request):
        form = requestForm(request.POST)
        if form.is_valid():
            form.save()
            car = form.cleaned_data['car']
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            violation_type = form.cleaned_data['violation_type']
            comments = form.cleaned_data['comments']
        context = {
            'form': form,
            'car': car,
            'longitude': longitude,
            'latitude': latitude,
            'violation_type': violation_type,
            'comments': comments,
        }

        return render(
            request=request,
            template_name='viols/new-violation.html',
            context=context
            )


class newCar(View):
    def get(self, request):
        form = carForm()
        context = {
            'form': form,
            }

        return render(
            request=request,
            template_name='cars/car-register.html',
            context=context
            )

    def post(self, request):
        form = carForm(request.POST)
        if form.is_valid():
            form.save()
            car_id = form.cleaned_data['car_id']
            car_type = form.cleaned_data['car_type']
            num_passengers = form.cleaned_data['num_passengers']
            car_owner = form.cleaned_data['car_owner']
            plate_num = form.cleaned_data['plate_num']
        context = {
            'form': form,
            'car_id': car_id,
            'car_type': car_type,
            'num_passengers': num_passengers,
            'car_owner': car_owner,
            'plate_num': plate_num,
        }

        return render(
            request=request,
            template_name='cars/car-register.html',
            context=context
            )
