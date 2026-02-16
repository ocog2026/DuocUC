"""
RUTAS Y VISTAS DE LA APLICACIÓN - app/routes.py
Este archivo define las rutas (URLs) de la aplicación y las funciones que se ejecutan
cuando el usuario accede a cada URL (vistas).

PASO 3: Crear las rutas para las operaciones CRUD
Las rutas mapean URLs a funciones Python.
Ejemplo: GET /clientes → obtener_todos_clientes()
"""

from flask import render_template, request, redirect, url_for, flash
from . import models


# ============================================================================
# RUTA: PÁGINA DE INICIO - LISTAR TODOS LOS CLIENTES
# ============================================================================
def listar_clientes():
    """
    Muestra la lista de todos los clientes.
    
    EXPLICACIÓN:
    - URL: / o /clientes
    - Método HTTP: GET
    - Acción: Obtiene todos los clientes de la BD y los muestra en la página
    - Template: templates/index.html
    
    FLUJO:
    1. Llama a models.obtener_todos_clientes()
    2. Pasa los clientes al template index.html
    3. El template HTML muestra los clientes en una tabla
    
    RETORNA:
    - HTML renderizado con la lista de clientes
    """
    # Llamar a la función del modelo para obtener todos los clientes
    clientes = models.obtener_todos_clientes()
    
    # Renderizar el template HTML pasándole los clientes
    return render_template('index.html', clientes=clientes)


# ============================================================================
# RUTA: MOSTRAR FORMULARIO PARA AGREGAR CLIENTE
# ============================================================================
def mostrar_formulario_agregar():
    """
    Muestra el formulario para agregar un nuevo cliente.
    
    EXPLICACIÓN:
    - URL: /clientes/agregar
    - Método HTTP: GET
    - Acción: Muestra un formulario HTML vacío
    - Template: templates/agregar.html
    
    FLUJO:
    1. El usuario hace clic en "Agregar Cliente"
    2. Se accede a la ruta /clientes/agregar
    3. Se muestra el formulario
    
    RETORNA:
    - HTML con el formulario
    """
    return render_template('agregar.html')


# ============================================================================
# RUTA: PROCESAR FORMULARIO Y AGREGAR CLIENTE (CREATE)
# ============================================================================
def agregar_cliente():
    """
    Procesa el formulario y agrega un nuevo cliente a la base de datos.
    
    EXPLICACIÓN:
    - URL: /clientes/agregar
    - Método HTTP: POST (cuando se envía el formulario)
    - Acción: Toma los datos del formulario y los inserta en la BD
    
    FLUJO:
    1. El usuario rellena el formulario y hace clic en "Guardar"
    2. Se envían los datos por POST
    3. Se obtienen los datos con request.form
    4. Se validan los datos
    5. Se llama a models.agregar_cliente()
    6. Se muestra un mensaje de éxito y se redirecciona
    
    RETORNA:
    - Redirecciona a /clientes (página de lista)
    """
    # Obtener los datos del formulario enviado por POST
    # request.form es un diccionario con los datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    
    # Validación básica: verificar que no estén vacíos
    if not nombre or not email or not telefono or not direccion:
        # Si faltan campos, mostrar un mensaje de error
        flash('⚠️ Todos los campos son obligatorios', 'error')
        return redirect(url_for('agregar_cliente_form'))
    
    # Llamar a la función del modelo para insertar en la BD
    if models.agregar_cliente(nombre, email, telefono, direccion):
        # Si fue exitoso, mostrar mensaje de éxito
        flash(f'✓ Cliente "{nombre}" agregado exitosamente', 'exito')
        return redirect(url_for('listar_clientes'))
    else:
        # Si hubo error, mostrar mensaje de error
        flash('✗ Error al agregar el cliente', 'error')
        return redirect(url_for('agregar_cliente_form'))


# ============================================================================
# RUTA: MOSTRAR FORMULARIO PARA EDITAR CLIENTE
# ============================================================================
def mostrar_formulario_editar(cliente_id):
    """
    Muestra el formulario para editar un cliente existente.
    
    EXPLICACIÓN:
    - URL: /clientes/editar/<cliente_id>
    - Método HTTP: GET
    - Acción: Obtiene los datos del cliente y muestra el formulario rellenado
    - Template: templates/editar.html
    - <cliente_id> es una variable en la URL (parámetro dinámico)
    
    FLUJO:
    1. El usuario hace clic en "Editar" en la tabla
    2. Se accede a /clientes/editar/5 (donde 5 es el ID del cliente)
    3. Se obtienen los datos del cliente de la BD
    4. Se muestra el formulario con los datos
    
    PARÁMETROS:
    - cliente_id (int): El ID del cliente a editar (viene en la URL)
    
    RETORNA:
    - HTML con el formulario rellenado
    """
    # Obtener los datos del cliente por ID
    cliente = models.obtener_cliente_por_id(cliente_id)
    
    # Si el cliente no existe, mostrar error
    if not cliente:
        flash('✗ Cliente no encontrado', 'error')
        return redirect(url_for('listar_clientes'))
    
    # Renderizar el template editar.html pasándole los datos del cliente
    return render_template('editar.html', cliente=cliente)


# ============================================================================
# RUTA: PROCESAR FORMULARIO Y ACTUALIZAR CLIENTE (UPDATE)
# ============================================================================
def actualizar_cliente(cliente_id):
    """
    Procesa el formulario y actualiza los datos de un cliente.
    
    EXPLICACIÓN:
    - URL: /clientes/editar/<cliente_id>
    - Método HTTP: POST
    - Acción: Toma los datos del formulario y actualiza la BD
    
    FLUJO:
    1. El usuario modifica los campos del formulario
    2. Hace clic en "Guardar cambios"
    3. Se envían los datos por POST
    4. Se llama a models.actualizar_cliente()
    5. Se muestra un mensaje y se redirecciona
    
    PARÁMETROS:
    - cliente_id (int): ID del cliente a actualizar
    
    RETORNA:
    - Redirecciona a /clientes
    """
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    
    # Validación básica
    if not nombre or not email or not telefono or not direccion:
        flash('⚠️ Todos los campos son obligatorios', 'error')
        return redirect(url_for('mostrar_formulario_editar', cliente_id=cliente_id))
    
    # Llamar a la función del modelo para actualizar
    if models.actualizar_cliente(cliente_id, nombre, email, telefono, direccion):
        flash(f'✓ Cliente actualizado exitosamente', 'exito')
        return redirect(url_for('listar_clientes'))
    else:
        flash('✗ Error al actualizar el cliente', 'error')
        return redirect(url_for('mostrar_formulario_editar', cliente_id=cliente_id))


# ============================================================================
# RUTA: ELIMINAR CLIENTE (DELETE)
# ============================================================================
def eliminar_cliente(cliente_id):
    """
    Elimina un cliente de la base de datos.
    
    EXPLICACIÓN:
    - URL: /clientes/eliminar/<cliente_id>
    - Método HTTP: POST (desde un botón en el formulario)
    - Acción: Elimina el cliente de la BD
    
    FLUJO:
    1. El usuario hace clic en "Eliminar"
    2. Se solicita confirmación
    3. Se envía POST a /clientes/eliminar/5
    4. Se llama a models.eliminar_cliente()
    5. Se muestra un mensaje y se redirecciona
    
    PARÁMETROS:
    - cliente_id (int): ID del cliente a eliminar
    
    RETORNA:
    - Redirecciona a /clientes
    """
    # Llamar a la función del modelo para eliminar
    if models.eliminar_cliente(cliente_id):
        flash(f'✓ Cliente eliminado exitosamente', 'exito')
    else:
        flash('✗ Error al eliminar el cliente', 'error')
    
    # Redireccionar a la lista de clientes
    return redirect(url_for('listar_clientes'))
