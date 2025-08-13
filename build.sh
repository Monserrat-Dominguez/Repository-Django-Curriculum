python - <<EOF
from dates.models import Perfil
if not Perfil.objects.exists():
    import os
    os.system('python manage.py loaddata dates/fixtures/datos.json')
EOF
