from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

@receiver(post_save, sender = Car)
def car_post_save(sender, instance, created, **kwargs):
    description = event_description(instance, created=created)
    car_inventory_update(description)
        

@receiver(post_delete, sender = Car)
def car_post_delete(sender, instance, **kwargs):
    """POST DELETE"""
    description = event_description(instance, deleted=True)
    car_inventory_update(description)
    


def car_inventory_update(description):
    """FUNCAO PARA QUANTIDADE DE CARROS E SOMA DOS VALORES DOS CARROS"""
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total=Sum('value'))['total']
    CarInventory.objects.create(cars_count = cars_count, cars_value = cars_value, event_description=description)



def event_description(instance, created=False, deleted=False):
    if deleted:
        action = 'deleção'
    elif created:
        action = 'criação'
    else:
        action = 'atualização'

    return f"Evento de {action} do carro {instance.model} (ID {instance.id}) - (Placa {instance.plate})"
