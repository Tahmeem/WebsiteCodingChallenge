"""image_access URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin #default import
from django.urls import path,include #imported to use our app
from django.conf import settings #for images
from django.conf.urls.static import static #for images

urlpatterns = [
    path('admin/', admin.site.urls), #route to admin
    path('',include('main_app.urls')), #main page
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #This is for when images are entered
