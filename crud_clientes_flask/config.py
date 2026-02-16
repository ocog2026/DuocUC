"""
CONFIGURACIÓN DE LA APLICACIÓN FLASK - config.py
Este archivo contiene las configuraciones principales de la aplicación,
especialmente la conexión a la base de datos MySQL.

PASO 1: Definir variables de conexión a la base de datos
Estas variables se utilizarán en toda la aplicación para conectarse a MySQL.
"""

# ============================================================================
# CONFIGURACIÓN DE BASE DE DATOS MYSQL
# ============================================================================
# Estas son las credenciales para conectarse a MySQL
# CAMBIAR ESTOS VALORES según tu instalación de MySQL

DB_HOST = 'localhost'           # Host del servidor MySQL (usualmente localhost)
DB_USER = 'root'                # Usuario de MySQL (por defecto 'root')
DB_PASSWORD = 'root'            # Contraseña de MySQL (cambiar si es diferente)
DB_NAME = 'crud_clientes_db'    # Nombre de la base de datos
DB_PORT = 3306                  # Puerto MySQL (por defecto 3306)

# ============================================================================
# CONFIGURACIÓN DE FLASK
# ============================================================================
# Configuraciones generales de la aplicación Flask

# Clave secreta para sesiones y tokens (cambiar en producción)
SECRET_KEY = 'clave_secreta_muy_segura_cambiar_en_produccion'

# Modo de depuración (True en desarrollo, False en producción)
DEBUG = True

# Ambiente (development, production, testing)
ENV = 'development'

# ============================================================================
# CONFIGURACIÓN DE VARIABLES GLOBALES
# ============================================================================

# Información sobre la aplicación
APP_NAME = 'CRUD Clientes Flask'
APP_VERSION = '1.0.0'
APP_DESCRIPTION = 'Aplicación para gestionar clientes con MySQL y Flask'
