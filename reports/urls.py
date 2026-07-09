from django.urls import path
from . import views

urlpatterns = [

    path('', views.reports_index, name='reports_index'), 
    path('empleados/', views.reporte_empleados, name='reporte_empleados'),
    path('empleados/pdf/', views.reporte_empleados_pdf, name='reporte_empleados_pdf'),
    path('inventario/materias_primas/', views.reporte_materias_primas, name='reporte_materias_primas'),
    path('inventario/materias_primas/pdf/', views.reporte_materias_primas_pdf, name='reporte_materias_primas_pdf'),
    path('inventario/productos/', views.reporte_productos, name='reporte_productos'),
    path('inventario/productos/pdf/', views.reporte_productos_pdf, name='reporte_productos_pdf'),

]