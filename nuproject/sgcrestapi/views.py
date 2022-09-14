from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
from .models import Articulos
from .models import SocioNegocios
from .models import CodProveedor
from .models import CabeceraFactura
from .models import LineasFactura
from .models import CentrodeCosto
from .models import SaldoInicialCDC

from .serializers import *

# Articulos Create y Read all

@api_view(['GET', 'POST'])
def lista_articulos(request):
    if request.method == 'GET':
        data = Articulos.objects.all()

        serializer = ArticulosSerializer(data, context= {'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ArticulosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Articulos Read One, Update, Delete

@api_view(['GET','POST','DELETE'])
def single_articulo(request, id):
    
    try:
        articulo = Articulos.objects.get(id=id)
    except Articulos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ArticulosSerializer(articulo, context= {'request': request}, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = ArticulosSerializer(articulo, data=request.data ,context= {'request': request}, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Socio de Negocios Read all, Create

@api_view(['GET','POST'])
def lista_sn(request):
    if request.method == 'GET':
        data = SocioNegocios.objects.all()

        serializer = SocioNegociosSerializer(data, context= {'request': request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':

        serializer = SocioNegociosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Socio de Negocios Read one, Update, Delete

@api_view(['GET','PUT','DELETE'])
def single_sn(request, id):
    
    try:
        sn = SocioNegocios.objects.get(id=id)
    except SocioNegocios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocioNegociosSerializer(sn, context= {'request': request}, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SocioNegociosSerializer(sn, data=request.data ,context= {'request': request}, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        sn.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Codigo de Proveedor Read All, Create

@api_view(['GET','POST'])
def lista_cod_prov(request):
    if request.method == 'GET':
        data = CodProveedor.objects.all()
        serializer = CodProveedorSerializer(data, context= {'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        serializer = CodProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# Codigo de Proveedor Filtro por articulo

@api_view(['GET'])
def articulo_cod_prov(request,id):
    try:
        data = CodProveedor.objects.filter(articulo_id=id)
    except Articulos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':    
        serializer = CodProveedorSerializer(data, context= {'request': request}, many=True)
        return Response(serializer.data)   

# Codigo de Proveedor Update, Delete
@api_view(['PUT','DELETE'])
def cod_prov_update_delete(request,id):
    try:
        data = CodProveedor.objects.get(id=id)
    except Articulos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CodProveedorSerializer(data, data=request.data ,context= {'request': request}, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# Saldo Inicial Read One, Create multiple lines, Delete multiple lines, Update multiple lines

@api_view(['GET','POST','PUT','DELETE'])
def saldo_inicial(request,id):
    
    try:
        data = SaldoInicialCDC.objects.filter(cdc=id)
    except SaldoInicialCDC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SaldoInicialCDCSerializer(data, context= {'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        alldata = []
        for record in request.data:
            serializer = SaldoInicialCDCSerializer(data=record)
            if serializer.is_valid():
                alldata.append(serializer)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        for record in alldata:
            record.save()
        
        return Response(status=status.HTTP_201_CREATED)        

    elif request.method == 'PUT':
        listaregistros = []
        for record in request.data:
            try:
                registro = SaldoInicialCDC.objects.get(id=record["id"])
            except SaldoInicialCDC.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SaldoInicialCDCSerializer(registro, data=record,context= {'request': request}, many=False)
            listaregistros.append(serializer)
            
        for record in listaregistros:
            if record.is_valid():
                record.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED) 
    
    elif request.method == 'DELETE':
        for record in request.data:
            registro = SaldoInicialCDC.objects.get(id=record["id"])
            registro.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def centro_costo(request):
    if request.method == 'GET':
        data = CentrodeCosto.objects.all()

        serializer = CentrodeCostoSerializer(data, context= {'request': request}, many=True)

        return Response(serializer.data) 

    elif request.method == 'POST':

        serializer = CentrodeCostoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def facturas_all(request):
    if request.method == 'GET':
        facturas = 1