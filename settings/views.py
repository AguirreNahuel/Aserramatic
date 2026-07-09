import json
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile 

JSON_PATH = os.path.join(settings.BASE_DIR, 'settings/config.json')

@login_required
def settings_panel(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    puede_editar_global = False
    if request.user.rol and request.user.rol.puede_configurar:
        puede_editar_global = True

    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r') as f:
            config_global = json.load(f)
    else:
        config_global = {"auto_logout": False, "session_timeout": 60}

    if request.method == 'POST':
        # 1. Guardar Tema (Personal)
        profile.theme = request.POST.get('theme', 'light')
        profile.save()

        if puede_editar_global:
            config_global['auto_logout'] = 'auto_logout' in request.POST
            config_global['session_timeout'] = int(request.POST.get('timeout', 60))
            with open(JSON_PATH, 'w') as f:
                json.dump(config_global, f, indent=4)
            
        return redirect('settings_panel')

    context = {
        'config': config_global,
        'profile': profile,
        'puede_editar_global': puede_editar_global 
    }
    return render(request, 'settings/configuracion.html', context)