# settings/context_processors.py
from .utils import get_config
from .models import UserProfile

def global_settings(request):
    config_data = get_config()
    
    # Si el usuario está logueado, buscamos SU tema
    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        # Pisamos o añadimos el tema personal a los datos que van al HTML
        config_data['theme'] = profile.theme
    else:
        # Tema por defecto si no está logueado
        config_data['theme'] = 'light'
        
    return {'site_settings': config_data}