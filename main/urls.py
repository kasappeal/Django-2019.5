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

from photos.views import LatestPhotosView, PhotoDetailView, NewPhotoView, PhotoListView
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
    path('', LatestPhotosView.as_view(), name='home')
]
