# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bodega(models.Model):
    id_bodega = models.BigIntegerField(primary_key=True)
    num_pasillo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'bodega'


class Categoria(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'categoria'


class Ciudad(models.Model):
    id_ciudad = models.BigIntegerField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=30)
    codigo_postal = models.BigIntegerField()
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    genero = models.CharField(max_length=1)
    telÚfono = models.BigIntegerField()
    email = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'cliente'


class CuentaCliente(models.Model):
    email = models.CharField(primary_key=True, max_length=40)
    clave = models.CharField(max_length=20)
    cliente_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut')

    class Meta:
        managed = False
        db_table = 'cuenta_cliente'


class CuentaEmpleado(models.Model):
    usuario = models.CharField(primary_key=True, max_length=20)
    clave = models.CharField(max_length=20)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')
    empleado_rut = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        managed = False
        db_table = 'cuenta_empleado'


class DetalleOrden(models.Model):
    id_detalle_orden = models.BigIntegerField(primary_key=True)
    cantidad = models.BigIntegerField()
    precio = models.BigIntegerField()
    cuenta_cliente_email = models.ForeignKey(CuentaCliente, models.DO_NOTHING, db_column='cuenta_cliente_email')
    empleado_rut = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_rut')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id = models.BigIntegerField()
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=1)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=30)
    cargo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoPago(models.Model):
    id_estado_pago = models.BigIntegerField(primary_key=True)
    nombre_estado_pago = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_pago'


class EstadoPedido(models.Model):
    id_estado_pedido = models.BigIntegerField(primary_key=True)
    nombre_estado_pedido = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Estanteria(models.Model):
    id_estanteria = models.BigIntegerField(primary_key=True)
    capacidad = models.BigIntegerField()
    pasillo_id_pasillo = models.ForeignKey('Pasillo', models.DO_NOTHING, db_column='pasillo_id_pasillo')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estanteria'


class Marca(models.Model):
    id_marca = models.BigIntegerField(primary_key=True)
    nombre_marca = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'marca'


class Oferta(models.Model):
    id_oferta = models.BigIntegerField(primary_key=True)
    id_proveedor = models.BigIntegerField()
    nombre_proveedor = models.CharField(max_length=40)
    apellido_proveedor = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    oferta = models.CharField(max_length=300)
    fecha = models.DateField()
    empleado_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        managed = False
        db_table = 'oferta'


class OrdenCompra(models.Model):
    id_orden = models.BigIntegerField(primary_key=True)
    precio_total = models.BigIntegerField()
    fecha_compra = models.DateField()
    fecha_estimada = models.DateField()
    estado_pago_id_estado_pago = models.ForeignKey(EstadoPago, models.DO_NOTHING, db_column='estado_pago_id_estado_pago')
    detalle_orden_id_detalle_orden = models.ForeignKey(DetalleOrden, models.DO_NOTHING, db_column='detalle_orden_id_detalle_orden')
    estado_pedido_id_estado_pedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estado_pedido_id_estado_pedido')
    tipo_pago_id_tipo_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='tipo_pago_id_tipo_pago')
    id_tipo_pago = models.BigIntegerField()
    tipo_orden_id_tipo_orden = models.ForeignKey('TipoOrden', models.DO_NOTHING, db_column='tipo_orden_id_tipo_orden')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pasillo(models.Model):
    id_pasillo = models.BigIntegerField(primary_key=True)
    num_estanteria = models.BigIntegerField()
    bodega_id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='bodega_id_bodega')

    class Meta:
        managed = False
        db_table = 'pasillo'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    precio = models.BigIntegerField()
    stock = models.BigIntegerField()
    oferta = models.CharField(max_length=1)
    porcentaje = models.BigIntegerField(blank=True, null=True)
    marca_id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca_id_marca')
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_categoria')

    class Meta:
        managed = False
        db_table = 'producto'


class Region(models.Model):
    id_region = models.BigIntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rol'


class SolicitudPresencial(models.Model):
    id_producto = models.BigIntegerField()
    nombre_producto = models.CharField(max_length=30)
    cantidad = models.BigIntegerField()
    orden_compra_id_orden = models.OneToOneField(OrdenCompra, models.DO_NOTHING, db_column='orden_compra_id_orden', primary_key=True)

    class Meta:
        managed = False
        db_table = 'solicitud_presencial'


class SolicitudProductos(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    nombre_categoria = models.BigIntegerField()
    precio = models.BigIntegerField()
    nombre_marca = models.BigIntegerField()
    stock = models.BigIntegerField()
    observacion = models.CharField(max_length=30, blank=True, null=True)
    empleado_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        managed = False
        db_table = 'solicitud_productos'


class TipoOrden(models.Model):
    id_tipo_orden = models.BigIntegerField(primary_key=True)
    nombre_orden = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_orden'


class TipoPago(models.Model):
    id_tipo_pago = models.BigIntegerField(primary_key=True)
    nombre_pago = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class Valoracion(models.Model):
    id_valoracion = models.BigIntegerField(primary_key=True)
    valoracion = models.BigIntegerField()
    producto_id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'valoracion'
