from django import forms
from .models import Producto, MateriaPrima

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'materia_prima', 
            'espesor_pulgadas', 
            'ancho_pulgadas', 
            'largo_pies', 
            'cantidad_piezas'
        ]
        labels = {
            'materia_prima': 'Lote de Origen (Materia Prima)',
            'espesor_pulgadas': 'Espesor (pulg)',
            'ancho_pulgadas': 'Ancho (pulg)',
            'largo_pies': 'Largo (pies)',
        }

class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['especie', 'cantidad_rollizos', 'descripcion']