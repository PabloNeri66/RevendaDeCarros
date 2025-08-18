from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from cars.models import Car
from cars.forms import CarForm
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
    new_car_form = CarForm()

    return render(request, 'new_car.html')