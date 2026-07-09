from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)
    
    puede_ver = models.BooleanField(default=False, help_text="Permite ver listados y detalles")
    puede_editar = models.BooleanField(default=False, help_text="Permite crear y modificar registros")
    puede_borrar = models.BooleanField(default=False, help_text="Permite eliminar registros")
    puede_configurar = models.BooleanField(default=False, help_text="Permite cambiar ajustes de sesión y globales")

    def __str__(self):
        return self.nombre_rol

    def __str__(self):
        return self.nombre_rol

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni_cuil = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class User(AbstractUser):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.is_active = self.activo 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    def get_display_name(self):

            if self.empleado and self.empleado.nombre:
                return self.empleado.nombre
            return self.username
    
    def get_display_name2(self):
        if self.empleado and self.empleado.nombre:
            return f"{self.empleado.nombre} {self.empleado.apellido} - {self.empleado.dni_cuil}"
        return self.username