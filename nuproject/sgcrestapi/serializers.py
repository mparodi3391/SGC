from dataclasses import field
from rest_framework import serializers
from .models import Articulos
from .models import SocioNegocios
from .models import CodProveedor
from .models import CentrodeCosto
from .models import SaldoInicialCDC
from .models import CabeceraFactura
from .models import LineasFactura

class ArticulosSerializer(serializers.ModelSerializer):

    class Meta:
        model=Articulos
        fields=('id','sku','descripcion','categoria','ult_precio_compra','marca')

class SocioNegociosSerializer(serializers.ModelSerializer):

    class Meta:
        model=SocioNegocios
        fields=('id','razon_social','nombre_fantasia','direccion','tipo_sn','tipo_doc_fiscal','doc_fiscal','telefono1','telefono2')

class CodProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model=CodProveedor
        fields=('id','cod_prov','articulo_id','socio_negocios_id')

class CentrodeCostoSerializer(serializers.ModelSerializer):

    class Meta:
        model=CentrodeCosto
        fields=('id','nombre','direccion','socio_negocios')

class SaldoInicialCDCSerializer(serializers.ModelSerializer):

    class Meta:
        model=SaldoInicialCDC
        fields=('id','articulo','cantidad','precio_cotizado','cdc')

class CabeceraFacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model=CabeceraFactura
        fields=('id','fecha_creacion','fecha_contabilizacion','sn','creador','comentario','cdc','estado','folio','subtotal','impuestos','total')

class LineasFacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model=LineasFactura
        fields=('id','factura','nro_linea','articulo','cantidad','precio','impuestos','moneda')
