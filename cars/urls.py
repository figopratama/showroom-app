from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [
    path('car-form/', views.newCar, name='car-form'),
    path('service-form/', views.newService, name='service-form'),
    path('<str:pk>/', views.detail, name='detail'),
]