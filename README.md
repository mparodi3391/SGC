# SGC

Sistema de Gestion de Compras.

El objetivo de este proyecto es crear una solucion para poder llevar de manera mas organizada y sencilla las compras de una empresa basada en proyectos.

La aplicacion constara de un Frontend desarrollados con Javascript, HTML y CSS, mientras que el backend sera enteramente desarrollado con Python usando el framework Django. El motor de Base de datos a utilizar es MySQL.
El Frontend, mediante Fetch API se conectara con el backend que tendra uno o mas endpoints generados por cada modulo, segun sean necesarios.

La aplicacion tendra los siguentes modulos:

1) Articulos
2) Socios de Negocios (Clientes y Proveedores)
3) Facturacion
4) Centros de Costo (Proyectos)
5) Saldos Iniciales

En el siguiente Apartado entraremos mas en detalle en las funcionalidades y especificaciones de cada modulo.

1) Articulos:

  Este modulo esta dedicado completamente a la creacion y busqueda de Articulos, los cuales formaran una parte crucial de la generacion de facturas y saldos iniciales.
  Se registran los datos basicos de cada productos como son un identificador unico (SKU), nombre, marca, y categoria.
  Ademas se registra el ultimo precio de compra, que se ira actualizando con las compras realizadas.

2) Socios de Negocios:
  
  Aqui se registraran todos los clientes y provedores de la compania con el fin de llevar un registro ordenado de la facturacion.
  Mantener esta distincion nos permitira en el futuro ampliar la aplicacion generando modulos de pago a proveedores y de facturacion a clientes.
  
3) Facturacion:

  Aqui se realizara el grueso de las operaciones del dia a dia, registrando las facturas que cada proveedor nos emita. 
  Las facturas en el lado del Backend estaran divididas en 2 partes, la cabecera de la factura donde se encuentra toda la informacion basica de las misma y las lineas donde se puede encontrar la informacion de cada producto adquirido.
  Se podran sacar reportes de facturacion como por ejemplo facturas por proveedor o ultimas compras de articulo bajo las necesidades del cliente.
  
4) Centros de Costo:

  Estos serviran como carpetas donde se iran almacenando las facturas relativas a cada proyecto. Esto en conjunto con el saldo inicial que se registrara permitira sacar reportes sobre el restante asignado para el proyecto.
  Ademas tendran informacion basica sobre el proyecto, como por ejemplo el cliente, la direccion en caso de que la haya y fecha de inicio y fin estimadas.

5) Saldos Iniciales:

  Tras la creacion del centro de costo se creara un Saldo Inicial asignado al mismo que permitira llevar una trazabilidad de los materiales restantes a utilizar en un proyecto determinado.
  Tambien, en el caso de que haya una cotizacion, se podra asignar un precio a cada articulo del saldo inicial, permitiendo ver si la cotizacion realizada fue correcta.
  
6) Reporteria:

  Mas alla de los reportes mencionados anteriormente, uno de los objetivos fundamentales del proyecto es permitirle a los usuarios la generacion de reportes basados en sus necesidades.
  La utilizacion de una base de datos relacional y un sistema de endpoints permite traer la informacion facilmente al frontend para su tratamiento.
  
Como conclusion, el proyecto busca brindarle profesionalismo al proceso de compras de una empresa, el cual generalemtne es subestimado en su importancia.
