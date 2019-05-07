from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from photos.models import Photo


def latest_photos(request):
    # Recuperar las últimas fotos de la base de datos
    photos = Photo.objects.all().order_by('-modification_date')

    # Creamos el contexto para pasarle las fotos a la plantilla
    context = {'latest_photos': photos[:5]}

    # Crear respuesta HTML con las fotos
    html = render(request, 'photos/latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)


def photo_detail(request, pk):
    # Recuperar la foto seleccionada de la base de datos
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return HttpResponseNotFound('Photo does not exist')

    # Crear un contexto para pasar la información a la plantilla
    context = {'photo': photo}

    # Renderizar plantilla
    html = render(request, 'photos/detail.html', context)

    # Devolver respuesta HTTP
    return HttpResponse(html)
