import os
import sys

# Adicionar o diretório do projeto ao path
INTERP = os.path.expanduser("~/virtualenv/sanyahudesigner/3.9/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
