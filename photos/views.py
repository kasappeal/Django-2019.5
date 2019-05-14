from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from photos.forms import PhotoForm
from photos.models import Photo


def latest_photos(request):
    # Recuperar las últimas fotos de la base de datos
    photos = Photo.objects.filter(visibility=Photo.PUBLIC).order_by('-modification_date')

    # Creamos el contexto para pasarle las fotos a la plantilla
    context = {'latest_photos': photos[:5]}

    # Crear respuesta HTML con las fotos
    html = render(request, 'photos/latest.html', context)

    # Devolver la respuesta HTTP
    return HttpResponse(html)


def photo_detail(request, pk):
    # Recuperar la foto seleccionada de la base de datos
    photo = get_object_or_404(Photo, pk=pk, visibility=Photo.PUBLIC)

    # Crear un contexto para pasar la información a la plantilla
    context = {'photo': photo}

    # Renderizar plantilla
    html = render(request, 'photos/detail.html', context)

    # Devolver respuesta HTTP
    return HttpResponse(html)


@login_required
def new_photo(request):
    if request.method == 'POST':
        photo = Photo()
        photo.owner = request.user
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            messages.success(request, 'Foto creada correctamente con ID {0}'.format(new_photo.pk))
            form = PhotoForm()
    else:
        form = PhotoForm()
    context = {'form': form}
    return render(request, 'photos/new.html', context)
