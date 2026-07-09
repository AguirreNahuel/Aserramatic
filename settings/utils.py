import json
import os
from django.conf import settings

JSON_PATH = os.path.join(settings.BASE_DIR, 'settings/config.json')

def get_config():
    with open(JSON_PATH, 'r') as f:
        return json.load(f)

def update_config(new_data):
    current_config = get_config()
    current_config.update(new_data)
    with open(JSON_PATH, 'w') as f:
        json.dump(current_config, f, indent=4)