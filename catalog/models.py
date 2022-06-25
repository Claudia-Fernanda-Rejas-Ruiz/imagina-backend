from django.db import models
from django.urls import reverse

# Create your models here.
import uuid 


class Cotiza(models.Model):
    cantidad=models.IntegerField()

class Cliente(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
         
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)

class CotizaInstance(models.Model):
    """
    Modelo que representa una copia específica de una fecha"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta fecha particular")
    cotiza = models.ForeignKey(Cotiza, on_delete=models.SET_NULL, null=True)
    nombre = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Disponibilidad de la fecha')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id)

