from django.urls import path
from . import views

urlpatterns = [

    path('', views.inventory_index, name='inventory_index'), 
    
    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Materia Prima
    path('materia-prima/', views.lista_materia_prima, name='lista_materia_prima'),
    path('materia-prima/nuevo/', views.crear_materia_prima, name='crear_materia_prima'),
    path('materia-prima/editar/<int:pk>/', views.editar_materia_prima, name='editar_materia_prima'),
    path('materia-prima/eliminar/<int:pk>/', views.eliminar_materia_prima, name='eliminar_materia_prima'),
    

]