from django.db import models

# Create your models here.

class CarInventory(models.Model):
    cars_count = models.IntegerField(verbose_name='Quantidade de carros')
    cars_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Dos Carros')
    created_at =  models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    event_description = models.TextField(blank=True, null=True, verbose_name='Descricao do evento')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'R${self.cars_value} para os {self.cars_count}.'



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['id', 'name']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name



class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True, verbose_name='Ano de fabricação')
    model_year = models.IntegerField(blank=True, null=True, verbose_name='Ano de modelo')
    plate = models.CharField(null=True, blank=True, max_length=10, verbose_name='Placa')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)



    class Meta:
        ordering = ['model']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'


    def upper_plate(self):
        if self.plate:
            self.plate = self.plate.upper()

    def hifen_plate(self):
        """
        Insere um hífen na placa veicular se o caractere na posição 4 NÃO for uma letra. Sendo uma placa antiga.
        """
        if not self.plate:
            return
        
        if "-" in self.plate:
            return
        
        caracteres_placa = list(self.plate)
        if len(caracteres_placa)> 5 and not caracteres_placa[4].isalpha():
            caracteres_placa.insert(3,"-")
        self.plate = "".join(caracteres_placa)


    def save(self, *args, **kwargs):
        self.upper_plate()
        self.hifen_plate()
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f'{self.brand} {self.model}'

    