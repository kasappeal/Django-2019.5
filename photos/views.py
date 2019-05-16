from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from photos.forms import PhotoForm
from photos.models import Photo


class LatestPhotosView(View):

    def get(self, request):
        # Recuperar las últimas fotos de la base de datos
        photos = Photo.objects.filter(visibility=Photo.PUBLIC).order_by('-modification_date').select_related('owner')

        # Creamos el contexto para pasarle las fotos a la plantilla
        context = {'latest_photos': photos[:5]}

        # Crear respuesta HTML con las fotos
        html = render(request, 'photos/latest.html', context)

        # Devolver la respuesta HTTP
        return HttpResponse(html)


class PhotoDetailView(View):

    def get(self, request, pk):
        # Recuperar la foto seleccionada de la base de datos
        photo = get_object_or_404(Photo.objects.select_related('owner'), pk=pk, visibility=Photo.PUBLIC)

        # Crear un contexto para pasar la información a la plantilla
        context = {'photo': photo}

        # Renderizar plantilla
        html = render(request, 'photos/detail.html', context)

        # Devolver respuesta HTTP
        return HttpResponse(html)


class NewPhotoView(LoginRequiredMixin, View):

    def get(self, request):
        form = PhotoForm()
        context = {'form': form}
        return render(request, 'photos/new.html', context)

    def post(self, request):
        photo = Photo()
        photo.owner = request.user
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            messages.success(request, 'Foto creada correctamente con ID {0}'.format(new_photo.pk))
            form = PhotoForm()
        context = {'form': form}
        return render(request, 'photos/new.html', context)


class PhotoList(object):

    def get_queryset(self):
        queryset = Photo.objects.select_related('owner').order_by('-modification_date')
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(visibility=Photo.PUBLIC)
        elif not self.request.user.is_superuser:
            queryset = queryset.filter(Q(visibility=Photo.PUBLIC) | Q(owner=self.request.user))
        return queryset


class PhotoListView(PhotoList, ListView):

    template_name = 'photos/list.html'

