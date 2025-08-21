from django.db.models import Q
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class CarsListView(ListView):
    """
    Listar Carros
    """
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'


    def get_queryset(self):
        cars = super().get_queryset().order_by('brand')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(Q(model__icontains=search) | Q(brand__name__icontains=search))
        return cars


class NewCarCreateView(CreateView):
    """
    Criar Carro
    """
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html' # ele entende o contexto por form por padrão
    success_url = '/cars/'


class CarDetailView(DetailView):
    """
    Detalhes do um Carro
    """
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    """
    Atualizar Carro
    """
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model=Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
