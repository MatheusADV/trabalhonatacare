"""
URL configuration for natalcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from .views import *

urlpatterns = [
    path('cadastro/', cadastrousuario.as_view(), name='cadastro'),
    path('procadu/', cadastrousuario.as_view(), name='procadu'),
    path('procadc/', cadastroclinica.as_view(), name='procadc'),
    path('login/', logusuario.as_view(), name='log'),
    path('prologu/', logusuario.as_view(), name='prologu'),
    path('prologc/', logclinica.as_view(), name='prologc'),
    path('', menu.as_view(), name='menu'),
    path('perfil/', perfil.as_view(), name="perfil"),
    path('properfil/', perfil.as_view(), name="properfil"),
    path('pesq/', resultados.as_view(), name="pesq"),
    path('logoutu/', logoutu.as_view(), name="logoutu"),
    path('msc/', mudar_senha_clin.as_view(), name="msc"),
    path('promsc/', mudar_senha_clin.as_view(), name="promsc"),
    path('clind/', clin_dados.as_view(), name="clinc"),
    path('clind/<int:id>/', clinusu.as_view(), name="clinu"),
    path('clined/', clinedit.as_view(), name="clined"),
    path('proclined/', clinedit.as_view(), name="proclined"),
    path('coment/<int:id>/', comentario.as_view(), name="coment"),
    path('favs/<int:id>/', favoritos.as_view(), name="favs"),
    path('chatusu/<int:id>/', chatusu.as_view(), name="chatusu"),
    path('chatclin/', chatclin.as_view(), name="chatclin"),
    path('prochatclin/<int:id>', prochatclin.as_view(), name="prochatclin"),
]
