from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from cars.models import Car
# Create your views here.

def cars_view(request: HttpRequest):
    cars = Car.objects.all()
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(request,
    'cars.html',
    {'cars': cars}
    )