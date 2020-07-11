"""Tarea_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from my_app.views import home, episode_view, character_view, location_view, searchBar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('episodio/<str:code>', episode_view, name='episode'),
    path('caracter/<int:id_character>', character_view, name='character'),
    path('lugar/<int:id_lugar>', location_view, name='location'),
    path('search/', searchBar, name='search')
]
