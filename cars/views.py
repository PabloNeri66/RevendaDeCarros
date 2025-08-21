from django.db.models import Q
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic.list import ListView
from django.views.generic import CreateView
# Create your views here.


class CarsListView(ListView):
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
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html' # ele entende o contexto por form por padrão
    success_url = '/cars/'


# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})
    

#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', {'new_car_form': new_car_form})
