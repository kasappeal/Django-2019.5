from django.http import HttpResponse
from django.shortcuts import render

from photos.models import Photo


def latest_photos(request):
    # Recuperar las últimas fotos de la base de datos
    photos = Photo.objects.all()

    # Creamos el contexto para pasarle las fotos a la plantilla
    context = {'latest_photos': photos}

    # Crear respuesta HTML con las fotos
    html = render(request, 'photos/latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)
