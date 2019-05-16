from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.models import Photo
from photos.permissions import PhotoPermission
from photos.serializers import PhotoListSerializer, PhotoSerializer
from photos.views import PhotoList


class PhotosAPI(PhotoList, ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return PhotoListSerializer if self.request.method == 'GET' else PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PhotoDetailAPI(PhotoList, RetrieveUpdateDestroyAPIView):

    permission_classes = [PhotoPermission]

    serializer_class = PhotoSerializer

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
