from django.urls import path, include
from . import views

urlpatterns = [
    # path('login', views.loginView.as_view(), name='login'),
    path('login/', views.loginView.as_view(), name='login'),

    # path('logout', views.LogoutView.as_view(), name="logout"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
