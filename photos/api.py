from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photos.permissions import PhotoPermission
from photos.serializers import PhotoListSerializer, PhotoSerializer
from photos.views import PhotoList


class PhotosViewSet(PhotoList, ModelViewSet):

    permission_classes = [PhotoPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'url', 'owner__first_name', 'owner__last_name']
    ordering_fields = ['id', 'creation_date', 'modification_date', 'name']

    def get_serializer_class(self):
        return PhotoListSerializer if self.action == 'list' else PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
