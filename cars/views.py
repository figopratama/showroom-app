from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

from .forms import NewCarForm, NewServiceForm
from .models import Car, Service

app_name = 'car'

def detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    services = Service.objects.filter(car=car)

    total_service_cost = services.aggregate(Sum('cost'))['cost__sum'] or 0

    loan = car.loan or 0
    interest = car.interest or 0
    denominator = loan + interest if (loan + interest) != 0 else 1
    production_cost = (car.price / denominator) + total_service_cost # Rumus HPP

    return render(request, 'car/detail.html', {
        'car': car,
        'services': services,
        'total_service_cost': total_service_cost,
        'production_cost': production_cost
    })

def newCar(request):
    if request.method == 'POST':
        form = NewCarForm(request.POST, request.FILES)

        if form.is_valid():
            car = form.save(commit=False)
            car.save()

            return redirect('car:detail', pk=car.plate_number) 
    else:
        form = NewCarForm()

    return render(request, 'car/car-form.html', {
        'form': form
    })

def newService(request):
    if request.method == 'POST':
        form = NewServiceForm(request.POST, request.FILES)

        if form.is_valid():
            service = form.save(commit=False)
            service.save()

            return redirect('car:detail', pk=service.car.plate_number) 
    else:
        form = NewServiceForm()

    return render(request, 'car/service-form.html', {
        'form': form
    })

