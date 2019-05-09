from django.forms import ModelForm

from photos.models import Photo


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['name', 'url', 'description', 'license', 'visibility']
