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

from photos.views import latest_photos, photo_detail, new_photo
from users.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # Users
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    # Photos
    path('photos/new/', new_photo, name='new_photo'),
    path('photos/<int:pk>/', photo_detail, name='photo_detail'),
    path('', latest_photos, name='home')
]
