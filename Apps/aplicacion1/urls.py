"""login1 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import Informacion1View,Informacion2View,UsuarioView,IngresarProductoView
from .views import ListaProductosView

app_name="App1" 

urlpatterns = [
    url(r'^$', Informacion1View.as_view(), name= 'inicio'),
    url(r'^Informacion$', Informacion2View.as_view(), name='informacion'),
    url(r'^usuario$', UsuarioView.as_view(), name='usuario'),
    url(r'^AddProducto$', IngresarProductoView.as_view(), name='AddProducto'),
    url(r'^ListaProducto$', ListaProductosView.as_view(), name='ListaProducto'),
    #url(r'^EditarProducto(?P<id>\d+)$', producto_editar.as_view(), name='EditarProducto'),
]
