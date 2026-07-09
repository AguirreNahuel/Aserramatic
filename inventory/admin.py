from django.contrib import admin
from .models import MateriaPrima, Producto

# Register your models here.

@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('especie', 'cantidad_rollizos', 'fecha_ingreso')
    list_filter = ('especie', 'fecha_ingreso')
    search_fields = ('especie', 'descripcion')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_especie', 'cantidad_piezas', 'get_pies_tablares')
    list_filter = ('materia_prima__especie',)
    search_fields = ('nombre', 'materia_prima__especie')

    def get_especie(self, obj):
        return obj.materia_prima.especie
    get_especie.short_description = 'Especie'
    get_especie.admin_order_field = 'materia_prima__especie'

    def get_pies_tablares(self, obj):
        return f"{obj.total_pies_tablares()} pt" 
    get_pies_tablares.short_description = 'Pies Tablares Totales'