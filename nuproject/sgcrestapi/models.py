from django.db import models

# Create your models here.

class Articulos(models.Model):
    sku = models.CharField("SKU", max_length=12, unique=True)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField("Document", max_length=20)
    ult_precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    marca = models.CharField("Marca", max_length=20)

class SocioNegocios(models.Model):
    razon_social = models.CharField("Razon Social", max_length=80)
    nombre_fantasia = models.CharField("Nombre de Fantasia", max_length=80)
    direccion = models.CharField("Direccion", max_length=240)
    tipo_sn = models.CharField("Tipo de SN", max_length=1)
    tipo_doc_fiscal = models.CharField("Tipo de Doc. fiscal", max_length=4)
    doc_fiscal = models.BigIntegerField(unique=True)
    telefono1 = models.IntegerField()
    telefono2 = models.IntegerField(null=True)

class CodProveedor(models.Model):
    cod_prov = models.CharField("Codigo de Proveedor", max_length=20)
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    socio_negocios = models.ForeignKey(SocioNegocios, on_delete=models.CASCADE)

class CentrodeCosto(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    direccion = models.CharField("Direccion", max_length=100)
    socio_negocios = models.ForeignKey(SocioNegocios, on_delete=models.CASCADE)

class SaldoInicialCDC(models.Model):
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_cotizado = models.DecimalField(max_digits=8, decimal_places=2)
    cdc = models.ForeignKey(CentrodeCosto, on_delete=models.CASCADE)

class CabeceraFactura(models.Model):
    fecha_creacion = models.DateTimeField()
    fecha_contabilizacion = models.DateField()
    creador = models.CharField("Creador", max_length=20)
    comentario = models.CharField("Comentario", max_length=256)
    cdc = models.ForeignKey(CentrodeCosto, on_delete=models.CASCADE)
    estado = models.CharField("Estado", max_length=1)
    folio = models.CharField("Numero de Folio", max_length=15)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class LineasFactura(models.Model):
    factura = models.ForeignKey(CabeceraFactura, on_delete=models.CASCADE)
    nro_linea = models.IntegerField()
    articulo = models.ForeignKey(Articulos, on_delete=models.RESTRICT)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField("Moneda", max_length=3)
    






