"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from sgcrestapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/articulos/$', views.lista_articulos),
    re_path(r'^api/articulos/([0-9]+)$', views.single_articulo),
    re_path(r'^api/SN/$', views.lista_sn),
    re_path(r'^api/SN/([0-9]+)$', views.single_sn),
    re_path(r'^api/CodProv/$', views.lista_cod_prov),
    re_path(r'^api/CodProv/([0-9]+)$', views.articulo_cod_prov),
    re_path(r'^api/CodProvCRUD//([0-9]+)$', views.cod_prov_update_delete),
    re_path(r'^api/CDC/([0-9]+)$', views.saldo_inicial),
    re_path(r'^api/CDC/$', views.centro_costo),
    re_path(r'^api/facturas/$', views.facturas_all),
    re_path(r'^api/facturas/SN/([0-9]+)$', views.facturas_por_sn),
    re_path(r'^api/lineas_factura/([0-9]+)$', views.lineas_facturas)



]
