"""
MODELOS Y FUNCIONES DE BASE DE DATOS - app/models.py
Este archivo contiene las funciones para interactuar con la base de datos MySQL.
Cada función representa una operación CRUD (Create, Read, Update, Delete).

PASO 2: Crear funciones para acceder a la base de datos
"""

import mysql.connector
from mysql.connector import Error
import sys
import os

# Agregar la carpeta padre al path para importar config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


# ============================================================================
# FUNCIÓN PARA CONECTAR A LA BASE DE DATOS
# ============================================================================
def get_database_connection():
    """
    Crea una conexión a la base de datos MySQL.
    
    EXPLICACIÓN:
    - Esta función intenta conectarse a MySQL usando los datos de config.py
    - Si hay error, retorna None
    - Si la conexión es exitosa, retorna el objeto conexión
    
    RETORNA:
    - mysql.connector.MySQLConnection: objeto de conexión
    - None: si hay error en la conexión
    """
    try:
        # Crear conexión usando los parámetros de config.py
        conexion = mysql.connector.connect(
            host=config.DB_HOST,           # localhost
            user=config.DB_USER,           # root
            password=config.DB_PASSWORD,   # tu contraseña
            database=config.DB_NAME,       # crud_clientes_db
            port=config.DB_PORT            # 3306
        )
        # Si la conexión es exitosa, retornar el objeto
        if conexion.is_connected():
            print(f"✓ Conexión exitosa a MySQL")
            return conexion
    except Error as e:
        # Si hay error, mostrar el mensaje
        print(f"✗ Error al conectar a MySQL: {e}")
        return None


# ============================================================================
# OPERACIÓN CREATE: AGREGAR UN NUEVO CLIENTE
# ============================================================================
def agregar_cliente(nombre, email, telefono, direccion):
    """
    Inserta un nuevo cliente en la tabla 'clientes'.
    
    EXPLICACIÓN:
    - Recibe los datos del cliente como parámetros
    - Se conecta a la BD
    - Ejecuta un INSERT en la tabla clientes
    - Guarda los cambios (COMMIT)
    - Cierra la conexión
    
    PARÁMETROS:
    - nombre (str): Nombre del cliente
    - email (str): Correo electrónico del cliente
    - telefono (str): Teléfono del cliente
    - direccion (str): Dirección del cliente
    
    RETORNA:
    - bool: True si se agregó exitosamente, False si hubo error
    """
    try:
        # Paso 1: Obtener conexión a la BD
        conexion = get_database_connection()
        if not conexion:
            return False
        
        # Paso 2: Crear un cursor (objeto para ejecutar consultas)
        cursor = conexion.cursor()
        
        # Paso 3: Escribir la consulta SQL INSERT
        # Los signos %s son placeholders para los valores (protege contra SQL injection)
        sql = """
        INSERT INTO clientes (nombre, email, telefono, direccion)
        VALUES (%s, %s, %s, %s)
        """
        
        # Paso 4: Ejecutar la consulta con los valores
        valores = (nombre, email, telefono, direccion)
        cursor.execute(sql, valores)
        
        # Paso 5: Guardar los cambios en la BD (COMMIT)
        conexion.commit()
        
        print(f"✓ Cliente '{nombre}' agregado exitosamente")
        
        # Paso 6: Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()
        
        return True
        
    except Error as e:
        print(f"✗ Error al agregar cliente: {e}")
        return False


# ============================================================================
# OPERACIÓN READ: OBTENER TODOS LOS CLIENTES
# ============================================================================
def obtener_todos_clientes():
    """
    Obtiene la lista de todos los clientes de la base de datos.
    
    EXPLICACIÓN:
    - Se conecta a la BD
    - Ejecuta un SELECT para obtener todos los registros
    - Convierte los resultados en una lista de diccionarios
    - Retorna la lista
    
    RETORNA:
    - list: Lista de diccionarios con los datos de cada cliente
            Cada diccionario tiene: id, nombre, email, telefono, direccion, fecha_creacion
    - list vacía: Si hay error o no hay clientes
    """
    try:
        # Paso 1: Obtener conexión
        conexion = get_database_connection()
        if not conexion:
            return []
        
        # Paso 2: Crear cursor
        cursor = conexion.cursor(dictionary=True)  # dictionary=True para obtener diccionarios
        
        # Paso 3: Escribir la consulta SQL SELECT
        sql = "SELECT * FROM clientes ORDER BY fecha_creacion DESC"
        
        # Paso 4: Ejecutar la consulta
        cursor.execute(sql)
        
        # Paso 5: Obtener todos los resultados
        clientes = cursor.fetchall()
        
        # Paso 6: Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        
        return clientes
        
    except Error as e:
        print(f"✗ Error al obtener clientes: {e}")
        return []


# ============================================================================
# OPERACIÓN READ: OBTENER UN CLIENTE POR ID
# ============================================================================
def obtener_cliente_por_id(cliente_id):
    """
    Obtiene los datos de un cliente específico por su ID.
    
    EXPLICACIÓN:
    - Se conecta a la BD
    - Ejecuta un SELECT WHERE id = cliente_id
    - Retorna el cliente encontrado o None
    
    PARÁMETROS:
    - cliente_id (int): El ID del cliente a buscar
    
    RETORNA:
    - dict: Diccionario con los datos del cliente
    - None: Si no se encuentra el cliente o hay error
    """
    try:
        # Paso 1: Obtener conexión
        conexion = get_database_connection()
        if not conexion:
            return None
        
        # Paso 2: Crear cursor
        cursor = conexion.cursor(dictionary=True)
        
        # Paso 3: Escribir la consulta con WHERE
        sql = "SELECT * FROM clientes WHERE id = %s"
        
        # Paso 4: Ejecutar con el ID del cliente
        cursor.execute(sql, (cliente_id,))
        
        # Paso 5: Obtener solo una fila (fetchone)
        cliente = cursor.fetchone()
        
        # Paso 6: Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        
        return cliente
        
    except Error as e:
        print(f"✗ Error al obtener cliente: {e}")
        return None


# ============================================================================
# OPERACIÓN UPDATE: ACTUALIZAR DATOS DE UN CLIENTE
# ============================================================================
def actualizar_cliente(cliente_id, nombre, email, telefono, direccion):
    """
    Actualiza los datos de un cliente existente.
    
    EXPLICACIÓN:
    - Se conecta a la BD
    - Ejecuta un UPDATE WHERE id = cliente_id
    - Guarda los cambios (COMMIT)
    
    PARÁMETROS:
    - cliente_id (int): ID del cliente a actualizar
    - nombre (str): Nuevo nombre
    - email (str): Nuevo email
    - telefono (str): Nuevo teléfono
    - direccion (str): Nueva dirección
    
    RETORNA:
    - bool: True si se actualizó, False si hay error
    """
    try:
        # Paso 1: Obtener conexión
        conexion = get_database_connection()
        if not conexion:
            return False
        
        # Paso 2: Crear cursor
        cursor = conexion.cursor()
        
        # Paso 3: Escribir la consulta UPDATE
        sql = """
        UPDATE clientes 
        SET nombre = %s, email = %s, telefono = %s, direccion = %s 
        WHERE id = %s
        """
        
        # Paso 4: Ejecutar con los nuevos valores
        valores = (nombre, email, telefono, direccion, cliente_id)
        cursor.execute(sql, valores)
        
        # Paso 5: Guardar cambios
        conexion.commit()
        
        # Paso 6: Obtener el número de filas afectadas
        filas_afectadas = cursor.rowcount
        
        print(f"✓ Cliente actualizado ({filas_afectadas} fila(s) modificada(s))")
        
        # Paso 7: Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        
        return filas_afectadas > 0
        
    except Error as e:
        print(f"✗ Error al actualizar cliente: {e}")
        return False


# ============================================================================
# OPERACIÓN DELETE: ELIMINAR UN CLIENTE
# ============================================================================
def eliminar_cliente(cliente_id):
    """
    Elimina un cliente de la base de datos.
    
    EXPLICACIÓN:
    - Se conecta a la BD
    - Ejecuta un DELETE WHERE id = cliente_id
    - Guarda los cambios (COMMIT)
    
    PARÁMETROS:
    - cliente_id (int): ID del cliente a eliminar
    
    RETORNA:
    - bool: True si se eliminó, False si hay error
    """
    try:
        # Paso 1: Obtener conexión
        conexion = get_database_connection()
        if not conexion:
            return False
        
        # Paso 2: Crear cursor
        cursor = conexion.cursor()
        
        # Paso 3: Escribir la consulta DELETE
        sql = "DELETE FROM clientes WHERE id = %s"
        
        # Paso 4: Ejecutar el DELETE
        cursor.execute(sql, (cliente_id,))
        
        # Paso 5: Guardar cambios
        conexion.commit()
        
        # Paso 6: Obtener el número de filas afectadas
        filas_afectadas = cursor.rowcount
        
        print(f"✓ Cliente eliminado ({filas_afectadas} fila(s) eliminada(s))")
        
        # Paso 7: Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        
        return filas_afectadas > 0
        
    except Error as e:
        print(f"✗ Error al eliminar cliente: {e}")
        return False
