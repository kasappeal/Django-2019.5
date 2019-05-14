from django.core.exceptions import ValidationError
from django.forms import ModelForm

from photos.models import Photo


class PhotoForm(ModelForm):

    class Meta:
        model = Photo
        fields = ['name', 'url', 'description', 'license', 'visibility']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        BADWORDS = ['fuck', 'bastard', 'asshole', 'shit', 'Abollao', 'Limpiatubos', 'Mascachapas']
        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('{0} is a badword'.format(badword))
        return description
