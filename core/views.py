from django.shortcuts import render

from cars.models import Car, Service

def index(request):
    cars = Car.objects.all()
    services = Service.objects.filter() [0:6]

    return render(request, 'core/index.html', {
        'cars': cars,
        'services': services,
    })

def contact(request):
    return render(request, 'core/contact.html')