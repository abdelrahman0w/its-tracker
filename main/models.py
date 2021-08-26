from django.db import models
from django.db.models.deletion import SET_NULL
from datetime import datetime


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


class Car(models.Model):
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    car_id = models.CharField(verbose_name='Car ID', max_length=10000, primary_key=True, unique=True)
    car_type = models.CharField(verbose_name='Car Type', max_length=255, choices=CAR_TYPE)
    num_passengers = models.IntegerField(verbose_name='Number of Passengers', default=4)
    car_owner = models.CharField(verbose_name='Car Owner', max_length=255)
    plate_num = models.CharField(verbose_name='Plate Number', max_length=255)

    def __str__(self) -> str:
        return 'Car: ' + self.car_id


class Violation(models.Model):
    class Meta:
        verbose_name = "Violation"
        verbose_name_plural = "Violations"

    time_stamp = models.DateTimeField(default=datetime.now, blank=True)
    car = models.ForeignKey(to='Car', on_delete=models.CASCADE)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    violation_type = models.CharField(max_length=255, choices=VIO_TYPE)
    comments = models.TextField(max_length=555, default='N/A')

    def __str__(self) -> str:
        return 'Car: ' + self.car.car_id + ', ' + self.violation_type


class Traffic(models.Model):
    class Meta:
        verbose_name = "Traffic System"
        verbose_name_plural = "Traffic Systems"

    street = models.CharField(max_length=1000)
    additional = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.street + ' ST. Traffic System.'
