"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from files.views import FileViewSet
from photos.api import PhotosViewSet
from photos.views import LatestPhotosView, PhotoDetailView, NewPhotoView, PhotoListView
from users.api import UsersViewSet
from users.views import LoginView, LogoutView

router = SimpleRouter()
router.register('api/photos', PhotosViewSet, basename='photos_api')
router.register('api/users', UsersViewSet, basename='users_api')
router.register('api/files', FileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # Photos
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('photos/new/', NewPhotoView.as_view(), name='new_photo'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('', LatestPhotosView.as_view(), name='home'),
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
