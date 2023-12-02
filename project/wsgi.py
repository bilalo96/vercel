import os
import sys
from django.core.wsgi import get_wsgi_application

virtual_env = '/var/www/.virtualenvs/cp'

# Modify sys.path to include the directories within the virtual environment
sys.path = [
    f'{virtual_env}/lib/python3.10',
    f'{virtual_env}/lib/python3.10/plat-linux',
    f'{virtual_env}/lib/python3.10/lib-dynload',
    f'{virtual_env}/lib/python3.10/site-packages',
    # Add other paths if necessary
] + sys.path

# Add the Django project path to sys.path
sys.path.insert(0, '/var/www/django_projects/project')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Get the WSGI application
application = get_wsgi_application()

# Use 'application' as the WSGI callable
app = application
