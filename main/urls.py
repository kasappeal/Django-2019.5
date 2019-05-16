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
from django.contrib import admin
from django.urls import path

from photos.api import PhotosAPI, PhotoDetailAPI
from photos.views import LatestPhotosView, PhotoDetailView, NewPhotoView, PhotoListView
from users.api import UsersAPI, UserDetailAPI
from users.views import LoginView, LogoutView

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
    # API
    path('api/users/<int:pk>', UserDetailAPI.as_view(), name='user_detail_api'),
    path('api/users/', UsersAPI.as_view(), name='users_api'),
    path('api/photos/<int:pk>', PhotoDetailAPI.as_view(), name='photo_detail_api'),
    path('api/photos/', PhotosAPI.as_view(), name='photos_api')
]
