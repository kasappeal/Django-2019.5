from rest_framework.serializers import ModelSerializer

from files.models import File


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ['file']
