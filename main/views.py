from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


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


def newViolation(request):
    return render(request=request, template_name='viols/new-violation.html')