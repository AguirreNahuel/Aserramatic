from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import User, Empleado, Rol
from .forms import CustomUserCreationForm, CustomUserChangeForm, EmpleadoForm, RolForm


# --- VISTA DEL CHISTE ---
@login_required
def pagina_chiste(request):
    """Vista para trollear a los que intentan entrar por URL sin permiso de ver."""
    return render(request, 'buen_intento.html')

# --- VERIFICADORES DE PERMISOS ---
def puede_ver(u):
    if u.is_superuser: return True
    return u.is_authenticated and u.activo and (u.rol.puede_ver if u.rol else False)

def puede_editar(u):
    if u.is_superuser: return True
    return u.is_authenticated and u.activo and (u.rol.puede_editar if u.rol else False)

def puede_borrar(u):
    if u.is_superuser: return True
    return u.is_authenticated and u.activo and (u.rol.puede_borrar if u.rol else False)


# --- VISTAS DE USUARIOS ---

@login_required
def user_list(request):

    usuarios = User.objects.select_related('empleado', 'rol').all() if puede_ver(request.user) else []
    return render(request, 'users/user_list.html', {'usuarios': usuarios})

@login_required
def user_create(request):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form})

@login_required
def user_edit(request, pk):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
        
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=usuario)
    return render(request, 'users/user_form.html', {
        'form': form, 
        'editando': True, 
        'usuario_obj': usuario
    })

@login_required
def user_delete(request, pk):
    if not puede_ver(request.user) or not puede_borrar(request.user):
        return redirect('pagina_chiste')
        
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'usuario': usuario})


# --- VISTAS DE EMPLEADOS ---

@login_required
def empleado_list(request):
    empleados = Empleado.objects.all() if puede_ver(request.user) else []
    return render(request, 'users/empleado_list.html', {'empleados': empleados})

@login_required
def empleado_create(request):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
        
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'users/empleado_form.html', {'form': form})

@login_required
def empleado_update(request, pk):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
        
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'users/empleado_form.html', {'form': form})

@login_required
def empleado_delete(request, pk):
    if not puede_ver(request.user) or not puede_borrar(request.user):
        return redirect('pagina_chiste')
        
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_list')
    return render(request, 'users/empleado_confirm_delete.html', {'empleado': empleado})


# --- VISTAS DE ROLES ---

@login_required
def rol_list(request):
    roles = Rol.objects.all() if puede_ver(request.user) else []
    return render(request, 'users/rol_list.html', {'roles': roles})

@login_required
def rol_create(request):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
        
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rol_list')
    else:
        form = RolForm()
    return render(request, 'users/rol_form.html', {'form': form})

@login_required
def rol_edit(request, pk):
    if not puede_ver(request.user) or not puede_editar(request.user):
        return redirect('pagina_chiste')
        
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('rol_list')
    else:
        form = RolForm(instance=rol)
    return render(request, 'users/rol_form.html', {'form': form})

@login_required
def rol_delete(request, pk):
    if not puede_ver(request.user) or not puede_borrar(request.user):
        return redirect('pagina_chiste')
        
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        rol.delete()
        return redirect('rol_list')
    return render(request, 'users/rol_confirm_delete.html', {'rol': rol})


# --- INDEX ---

@login_required
def user_index(request):
    if not request.user.activo:
        raise PermissionDenied
        
    return render(request, 'users/user_index.html', {
        'usuarios_qty': User.objects.count(),
    })
