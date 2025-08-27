from django.db.models import Q
from django.shortcuts import render
from cars.models import Car, CarInventory
from cars.forms import CarModelForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
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



class CarDetailView(DetailView):
    """
    Detalhes do um Carro
    """
    model = Car
    template_name = 'car_detail.html'



@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    """
    Criar Carro
    """
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html' # ele entende o contexto por form por padrão
    success_url = '/cars/'



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    """
    Atualizar Carro
    """
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'


    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    """DELETAR UM CARRO"""
    model=Car
    template_name = 'car_delete.html'
    success_url = '/cars/'



class CarGraphView(View):
    def get(self, request, **kwargs):

        today = timezone.now().date()
        last_7_days = [(today - timedelta(days=i)) for i in range(6, -1, -1)]

        labels = [d.strftime("%d/%m") for d in last_7_days]
        values_total = []
        values_count = []

        for day in last_7_days:
            day_end = timezone.make_aware(
                timezone.datetime.combine(day, timezone.datetime.max.time())
            )

            # Pega o último registro até o final do dia
            last_record = CarInventory.objects.filter(created_at__lte=day_end).order_by('-created_at').first()

            if last_record:
                values_total.append(last_record.cars_value)
                values_count.append(last_record.cars_count)  # supondo que exista esse campo
            else:
                values_total.append(0)
                values_count.append(0)

        context = {
            "last_7_days": labels,
            "x_values1": values_total,  # valor total acumulado (último do dia)
            "x_values2": values_count,  # quantidade de carros acumulada
        }

        return render(request, template_name='car_graph.html', context=context)



