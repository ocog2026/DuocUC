"""
SCRIPT PARA CREAR LA BASE DE DATOS - setup_database.py
Este script crea la base de datos MySQL y la tabla de clientes.

PASO 0: Ejecutar este script ANTES de iniciar la aplicación
"""

import mysql.connector
from mysql.connector import Error
import sys

# ============================================================================
# CONFIGURACIÓN DE CONEXIÓN A MYSQL
# ============================================================================
# Cambiar estos valores según tu instalación

DB_HOST = 'localhost'      # Host del servidor MySQL
DB_USER = 'root'           # Usuario MySQL
DB_PASSWORD = 'root'       # Contraseña MySQL
DB_NAME = 'crud_clientes_db'  # Nombre de la BD a crear


def crear_base_datos():
    """
    Crea la base de datos y la tabla de clientes.
    
    EXPLICACIÓN:
    1. Se conecta a MySQL sin seleccionar BD
    2. Crea la BD crud_clientes_db
    3. Crea la tabla clientes con sus columnas
    4. Muestra mensajes de éxito
    """
    
    print("=" * 70)
    print("CREANDO BASE DE DATOS Y TABLA")
    print("=" * 70)
    print()
    
    try:
        # PASO 1: Conectar a MySQL (sin base de datos específica)
        print(f"[1/3] Conectando a MySQL en {DB_HOST}...")
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("✓ Conexión exitosa\n")
        
        # PASO 2: Crear la base de datos
        print(f"[2/3] Creando base de datos '{DB_NAME}'...")
        cursor = conexion.cursor()
        
        # SQL para crear la base de datos (IF NOT EXISTS evita errores si ya existe)
        sql_crear_bd = f"""
        CREATE DATABASE IF NOT EXISTS {DB_NAME}
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
        """
        cursor.execute(sql_crear_bd)
        print(f"✓ Base de datos '{DB_NAME}' creada/verificada\n")
        
        # PASO 3: Seleccionar la base de datos
        cursor.execute(f"USE {DB_NAME}")
        print(f"[3/3] Creando tabla 'clientes'...\n")
        
        # SQL para crear la tabla de clientes
        sql_crear_tabla = """
        CREATE TABLE IF NOT EXISTS clientes (
            -- COLUMNA ID: clave primaria, auto-incremento
            id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'ID único del cliente',
            
            -- COLUMNA NOMBRE: texto, obligatorio
            nombre VARCHAR(100) NOT NULL COMMENT 'Nombre del cliente',
            
            -- COLUMNA EMAIL: correo único
            email VARCHAR(100) NOT NULL UNIQUE COMMENT 'Email del cliente (único)',
            
            -- COLUMNA TELEFONO: texto, obligatorio
            telefono VARCHAR(20) NOT NULL COMMENT 'Teléfono del cliente',
            
            -- COLUMNA DIRECCION: texto largo
            direccion TEXT NOT NULL COMMENT 'Dirección del cliente',
            
            -- COLUMNA FECHA_CREACION: timestamp automático
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de creación',
            
            -- COLUMNA FECHA_ACTUALIZACION: se actualiza automáticamente
            fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
                ON UPDATE CURRENT_TIMESTAMP COMMENT 'Fecha de última actualización'
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        
        cursor.execute(sql_crear_tabla)
        print("✓ Tabla 'clientes' creada exitosamente\n")
        
        # PASO 4: Insertar datos de ejemplo (opcional)
        print("Insertando datos de ejemplo...")
        sql_insertar_ejemplo = """
        INSERT INTO clientes (nombre, email, telefono, direccion) 
        VALUES 
        ('Juan Pérez', 'juan@ejemplo.com', '+56 9 1234 5678', 'Calle Principal 123, Santiago'),
        ('María González', 'maria@ejemplo.com', '+56 9 2345 6789', 'Avenida Central 456, Santiago'),
        ('Carlos López', 'carlos@ejemplo.com', '+56 9 3456 7890', 'Calle Secundaria 789, Santiago')
        ON DUPLICATE KEY UPDATE email=email;
        """
        
        cursor.execute(sql_insertar_ejemplo)
        conexion.commit()
        print(f"✓ Se insertaron {cursor.rowcount} registros de ejemplo\n")
        
        # Mostrar información de la tabla
        cursor.execute("DESCRIBE clientes")
        columnas = cursor.fetchall()
        print("Estructura de la tabla 'clientes':")
        print("-" * 70)
        print(f"{'Campo':<20} {'Tipo':<30} {'Nulo':<10}")
        print("-" * 70)
        for col in columnas:
            campo = col[0]
            tipo = col[1]
            nulo = 'No' if col[2] == 'NO' else 'Sí'
            print(f"{campo:<20} {str(tipo):<30} {nulo:<10}")
        print("-" * 70)
        print()
        
        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        
        print("=" * 70)
        print("✓ BASE DE DATOS CREADA EXITOSAMENTE")
        print("=" * 70)
        print("Próximos pasos:")
        print("1. Verifica que MySQL esté corriendo")
        print("2. Ejecuta: python run.py")
        print("3. Abre en tu navegador: http://localhost:5000")
        print("=" * 70)
        return True
        
    except Error as e:
        print(f"✗ Error: {e}")
        print("\nSOLUCIONES:")
        print("- Verifica que MySQL esté corriendo")
        print("- Verifica el usuario y contraseña en config.py")
        print("- Verifica el nombre del host")
        return False


if __name__ == '__main__':
    # Ejecutar la creación de la base de datos
    if not crear_base_datos():
        sys.exit(1)
