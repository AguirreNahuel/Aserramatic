from django.db import models

class MateriaPrima(models.Model):
    especie = models.CharField(max_length=50) # Ej: Pino, Eucalipto
    cantidad_rollizos = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Rollizos de {self.especie} ({self.cantidad_rollizos} unidades)"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE, related_name='productos')
    
    espesor_pulgadas = models.DecimalField(max_digits=5, decimal_places=2)
    ancho_pulgadas = models.DecimalField(max_digits=5, decimal_places=2)
    largo_pies = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_piezas = models.IntegerField(default=0)
    
    def total_pies_tablares(self):
        return (self.espesor_pulgadas * self.ancho_pulgadas * self.largo_pies / 12) * self.cantidad_piezas

    def __str__(self):
        return f"{self.nombre} ({self.materia_prima.especie})"