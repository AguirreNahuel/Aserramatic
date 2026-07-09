from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),
    path('usuarios', views.user_list, name='user_list'),
    path('nuevo/', views.user_create, name='user_create'),
    path('editar/<int:pk>/', views.user_edit, name='user_edit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_update, name='empleado_update'),
    path('empleados/eliminar/<int:pk>/', views.empleado_delete, name='empleado_delete'),
    path('roles/', views.rol_list, name='rol_list'),
    path('roles/nuevo/', views.rol_create, name='rol_create'),
    path('roles/editar/<int:pk>/', views.rol_edit, name='rol_edit'),
    path('roles/eliminar/<int:pk>/', views.rol_delete, name='rol_delete'),
    path('Buen-Intento/', views.pagina_chiste, name='pagina_chiste'),
]