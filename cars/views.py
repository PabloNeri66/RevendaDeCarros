from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from cars.models import Car
from cars.forms import CarModelForm
# Create your views here.

def cars_view(request: HttpRequest):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(Q(model__icontains=search) | Q(brand__name__icontains=search))

    cars = cars.order_by('model')

    return render(request,
    'cars.html',
    {'cars': cars}
    )


def new_car_view(request: HttpRequest):
    
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')


    else:
        new_car_form = CarModelForm()
    return render(request,
        'new_car.html',
        {'new_car_form': new_car_form})