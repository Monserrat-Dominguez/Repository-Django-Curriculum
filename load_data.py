import json
from dates.models import Perfil, Historial, experiencia, FormacionComplementaria

def run():
    with open('datos.json', encoding='utf-8') as f:
        data = json.load(f)

    for p in data['perfiles']:
        perfil, created = Perfil.objects.get_or_create(
            email=p['email'],
            defaults={
                'nombre': p['nombre'],
                'telefono': p['telefono'],
                'ubicacion': p['ubicacion'],
                'resumen': p['resumen'],
                'imagen': p.get('imagen', None)
            }
        )

    for h in data['historiales']:
        Historial.objects.get_or_create(
            categoria=h['categoria'],
            titulo=h['titulo'],
            institucion=h['institucion'],
            ubicacion=h['ubicacion'],
            inicio=h['inicio'],
            fin=h.get('fin'),
            descripcion=h['descripcion']
        )

    for e in data['experiencias']:
        perfil = Perfil.objects.get(email=e['perfil_email'])
        experiencia.objects.get_or_create(
            perfil=perfil,
            puesto=e['puesto'],
            empresa=e['empresa'],
            description=e['description'],
            inicio=e.get('inicio'),
            fin=e.get('fin')
        )

    for f in data['formaciones']:
        perfil = Perfil.objects.get(email=f['perfil_email'])
        FormacionComplementaria.objects.get_or_create(
            perfil=perfil,
            curso=f['curso'],
            enlace=f['enlace']
        )

    print("✔ Datos cargados exitosamente.")
