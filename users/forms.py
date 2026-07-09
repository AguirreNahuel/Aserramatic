from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Empleado, Rol

# --- FORMULARIO DE CREACIÓN (REGISTRO) ---
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'empleado', 'rol', 'activo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

# --- FORMULARIO DE EDICIÓN (MODIFICAR) ---
class CustomUserChangeForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False, 
        label="Nueva Contraseña",
        help_text="Deje en blanco para mantener la contraseña actual."
    )

    class Meta:
        model = User
        fields = ('username', 'empleado', 'rol', 'activo')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        
        nueva_password = self.cleaned_data.get("password")
        
        if nueva_password:
            user.set_password(nueva_password)
        

        if commit:
            user.save()
        return user
    
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'dni_cuil']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni_cuil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 20-12345678-9'}),
        }

from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol', 'puede_ver', 'puede_editar', 'puede_borrar', 'puede_configurar']
        widgets = {
            'nombre_rol': forms.TextInput(attrs={'class': 'form-control'}),
            'puede_ver': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'puede_editar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'puede_borrar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'puede_configurar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }