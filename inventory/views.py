from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .models import Producto, MateriaPrima
from .forms import ProductoForm, MateriaPrimaForm

# --- VISTA INTERMEDIA (DASHBOARD DE INVENTARIO) ---
@login_required
def inventory_index(request):
    return render(request, 'inventory/inventory_index.html')


# --- VISTAS PARA PRODUCTO TERMINADO (TABLAS/MUEBLES) ---
@login_required
def lista_productos(request):
    productos = Producto.objects.all().select_related('materia_prima')
    return render(request, 'inventory/productos.html', {'productos': productos})


@login_required
def crear_producto(request):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_editar)):
        messages.error(request, "No tienes permisos de edición para registrar productos.")
        return redirect('lista_productos')
        
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto maderero registrado con éxito en el inventario.")
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventory/productos_form.html', {'form': form})


@login_required
def editar_producto(request, pk):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_editar)):
        messages.error(request, "No tienes permisos para modificar productos del inventario.")
        return redirect('lista_productos')
        
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f"Producto '{producto.nombre}' actualizado correctamente.")
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventory/productos_form.html', {'form': form, 'producto': producto})


@login_required
def eliminar_producto(request, pk):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_borrar)):
        messages.error(request, "Acción denegada. Tu rol de usuario no permite eliminar existencias.")
        return redirect('lista_productos')
        
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        try:
            nombre_eliminado = producto.nombre
            producto.delete()
            messages.warning(request, f"El producto '{nombre_eliminado}' ha sido removido del inventario físico.")
        except ProtectedError:
            messages.error(request, "No se puede eliminar este producto porque está asociado a registros protegidos del sistema.")
            
    return redirect('lista_productos')


# --- VISTAS PARA MATERIA PRIMA (ROLLIZOS/TRONCOS) ---
@login_required
def lista_materia_prima(request):
    materias_primas = MateriaPrima.objects.all()
    return render(request, 'inventory/materia_prima.html', {'materias_primas': materias_primas})


@login_required
def crear_materia_prima(request):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_editar)):
        messages.error(request, "No posees los permisos necesarios para ingresar materia prima.")
        return redirect('lista_materia_prima')
        
    if request.method == 'POST':
        form = MateriaPrimaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cargamento de rollizos ingresado correctamente al predio.")
            return redirect('lista_materia_prima')
    else:
        form = MateriaPrimaForm()
    return render(request, 'inventory/materiaPrima_form.html', {'form': form})


@login_required
def editar_materia_prima(request, pk):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_editar)):
        messages.error(request, "No tienes permisos para modificar el lote de materia prima.")
        return redirect('lista_materia_prima')
        
    material = get_object_or_404(MateriaPrima, pk=pk)
    if request.method == 'POST':
        form = MateriaPrimaForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, f"Lote de rollizos de {material.especie} modificado con éxito.")
            return redirect('lista_materia_prima')
    else:
        form = MateriaPrimaForm(instance=material)
    return render(request, 'inventory/materiaPrima_form.html', {'form': form, 'material': material})


@login_required
def eliminar_materia_prima(request, pk):
    if not (request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.puede_borrar)):
        messages.error(request, "Tu cuenta no tiene habilitado el permiso para dar de baja materia prima.")
        return redirect('lista_materia_prima')
        
    if request.method == 'POST':
        material = get_object_or_404(MateriaPrima, pk=pk)
        try:
            especie_eliminada = material.especie
            material.delete()
            messages.warning(request, f"El stock de rollizos de {especie_eliminada} ha sido eliminado.")
        except ProtectedError:
            # Clave: evita caídas del sistema si un rollizo ya fue aserrado en productos terminados
            messages.error(request, f"No se puede eliminar este lote de {material.especie} porque ya tiene productos terminados procesados vinculados a él.")
            
    return redirect('lista_materia_prima')