from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio
import logging

logger =  logging.getLogger("cars")



@receiver(pre_save, sender = Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        try:
            ai_bio = get_car_ai_bio(
                instance.model, instance.brand, instance.factory_year
            )
            instance.bio = ai_bio

        except Exception as e:
            logger.error(f"Erro ao gerar bio via IA para Car id={instance.id if instance.id else 'novo'}: {e}")
            instance.bio = 'Não declarado, Para saber mais: 11 99999999'



@receiver(post_save, sender = Car)
def car_post_save(sender, instance, created, **kwargs):
    """ POST SAVE """
    description = event_description(instance, created=created)
    car_inventory_update(description)
        

@receiver(post_delete, sender = Car)
def car_post_delete(sender, instance, **kwargs):
    """ POST DELETE """
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
