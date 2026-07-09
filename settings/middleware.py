from .utils import get_config

class DynamicSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Solo ejecutamos si el usuario está logueado
        if request.user.is_authenticated:
            config = get_config()
            
            # Si el checkbox de auto_logout está marcado en tu panel
            if config.get('auto_logout', False):
                # Obtenemos el tiempo del spinbox (minutos) y lo pasamos a segundos
                # Si por alguna razón no hay valor, usamos 600 segundos (10 min) por defecto
                timeout_minutes = int(config.get('session_timeout', 10))
                timeout_seconds = timeout_minutes * 60
                
                # Seteamos el tiempo de expiración de la sesión actual
                request.session.set_expiry(timeout_seconds)
        
        response = self.get_response(request)
        return response