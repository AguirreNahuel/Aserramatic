from django.shortcuts import render
from django.db.models import Sum
from users.models import User
from inventory.models import Producto, MateriaPrima


def home(request):
    conteo_personal_activo = User.objects.filter(activo=True).count()

    productos = Producto.objects.all()

    total_pies_tablares = sum(
        producto.total_pies_tablares() for producto in productos
    )

    total_rollizos = (
        MateriaPrima.objects.aggregate(
            total=Sum('cantidad_rollizos')
        )['total'] or 0
    )

    context = {
        'users_count': conteo_personal_activo,
        'total_pies_tablares': total_pies_tablares,
        'total_rollizos': total_rollizos,
    }

    return render(request, 'core/index.html', context)