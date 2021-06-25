from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/', views.index, name='index'),

    # path('cars', views.cars, name='cars'),
    path('cars/', views.cars, name='cars'),

    # path('cars/<str:car_id>', views.carDetail),
    path('cars/<str:car_id>/', views.carDetail),

    # path('car-register', views.carRegister, name='car-register'),
    path('car-register/', views.carRegister, name='car-register'),

    # path('violations', views.violations, name='violations'),
    path('violations/', views.violations, name='violations'),

    # path('traffics', views.traffics, name='traffics'),
    path('traffics/', views.traffics, name='traffics'),

    # path('dewDCW32feW3fsw-mdmD3mFa', views.newViolation, name='vio-form'),
    path('dewDCW32feW3fsw-mdmD3mFa/', views.newViolation.as_view(), name='vio-form'),
]
