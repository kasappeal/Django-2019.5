from rest_framework.serializers import ModelSerializer

from photos.models import Photo


class PhotoListSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = ['id', 'name', 'url']


class PhotoSerializer(ModelSerializer):

    class Meta:
        model = Photo
        fields = ['id', 'name', 'url', 'description', 'creation_date', 'modification_date',
                  'license', 'visibility', 'owner']
        read_only_fields = ['id', 'creation_date', 'modification_date']
