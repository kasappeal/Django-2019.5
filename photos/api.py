from rest_framework.generics import ListCreateAPIView

from photos.models import Photo
from photos.serializers import PhotoListSerializer, PhotoSerializer


class PhotosAPI(ListCreateAPIView):

    queryset = Photo.objects.all()

    def get_serializer_class(self):
        return PhotoListSerializer if self.request.method == 'GET' else PhotoSerializer
