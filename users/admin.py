from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Empleado, Rol

# Register your models here.


admin.site.register(Empleado)
admin.site.register(Rol)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información de Aserradero', {'fields': ('empleado', 'rol', 'activo')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de Aserradero', {'fields': ('empleado', 'rol', 'activo')}),
    )
    
    list_display = ('username', 'email', 'get_full_name_empleado', 'get_dni_empleado', 'rol', 'activo', 'is_staff')
    
    list_filter = ('rol', 'activo', 'is_staff', 'is_superuser')
    
    def get_full_name_empleado(self, obj):
        if obj.empleado:
            return f"{obj.empleado.nombre} {obj.empleado.apellido}" 
        return "Sin asignar"
    get_full_name_empleado.short_description = 'Nombre Empleado'

    def get_dni_empleado(self, obj):
        return obj.empleado.dni_cuil if obj.empleado else "-" 
    get_dni_empleado.short_description = 'DNI / CUIL'