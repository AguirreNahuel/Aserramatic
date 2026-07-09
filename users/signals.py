from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import User

@receiver(post_save, sender=User)
def asignar_grupo_por_rol(sender, instance, created, **kwargs):

    if instance.rol:

        group, _ = Group.objects.get_or_create(name=instance.rol.nombre_rol)
        
        instance.groups.clear()
        
        instance.groups.add(group)