from django.db import models

# Create your models here.
class Ciudad(models.Model):

    COUNTRIES = [
        ('CO', 'Colombia'),
    ]
    nombre = models.CharField(max_length=64)
    pais = models.CharField(max_length=64, choices=COUNTRIES)
    codigo = models.IntegerField()

    def __str__(self) -> str:
        return str(self.codigo) + " - " + self.nombre


class Aeropuerto(models.Model):

    nombre = models.CharField(max_length=64)
    codigo = models.CharField(max_length=3)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.codigo) + " -   " + self.nombre

class Vuelo(models.Model):
    origen = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT, related_name='origen')
    destino = models.ForeignKey(Aeropuerto, on_delete=models.PROTECT, related_name='destino')
    costo = models.FloatField()
    sillas = models.IntegerField()
    fecha_hora = models.DateTimeField()
