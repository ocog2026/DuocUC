-- ============================================================================
-- SCRIPT SQL PARA CREAR LA BASE DE DATOS Y TABLA
-- ============================================================================
-- Este archivo contiene las sentencias SQL para crear la base de datos manualmente
-- 
-- OPCIÓN 1: Ejecutar el script Python (recomendado)
-- $ python setup_database.py
--
-- OPCIÓN 2: Copiar y pegar este contenido en MySQL Workbench o línea de comandos
-- $ mysql -u root -p < schema.sql
-- ============================================================================

-- Paso 1: Crear la base de datos
-- DROP DATABASE IF EXISTS crud_clientes_db;  -- Descomenta para forzar reconstrucción
CREATE DATABASE IF NOT EXISTS crud_clientes_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Cambiar a la base de datos
USE crud_clientes_db;

-- Paso 2: Crear la tabla de clientes
CREATE TABLE IF NOT EXISTS clientes (
    -- ID: Clave primaria, auto-incremento
    id INT AUTO_INCREMENT PRIMARY KEY 
        COMMENT 'ID único del cliente',
    
    -- Nombre: Requerido, máximo 100 caracteres
    nombre VARCHAR(100) NOT NULL 
        COMMENT 'Nombre completo del cliente',
    
    -- Email: Requerido, único (no puede repetirse)
    email VARCHAR(100) NOT NULL UNIQUE 
        COMMENT 'Correo electrónico del cliente (debe ser único)',
    
    -- Teléfono: Requerido
    telefono VARCHAR(20) NOT NULL 
        COMMENT 'Teléfono de contacto del cliente',
    
    -- Dirección: Texto largo
    direccion TEXT NOT NULL 
        COMMENT 'Dirección física del cliente',
    
    -- Fecha de creación: Automática con fecha/hora actual
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        COMMENT 'Fecha y hora de creación del registro',
    
    -- Fecha de actualización: Se actualiza automáticamente
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP 
        COMMENT 'Fecha y hora de la última modificación'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Paso 3: Crear índices para mejorar búsquedas (opcional pero recomendado)
-- Índice en email para búsquedas rápidas
CREATE INDEX idx_email ON clientes(email);

-- Índice en nombre para búsquedas por nombre
CREATE INDEX idx_nombre ON clientes(nombre);

-- Índice en fecha de creación para ordenar
CREATE INDEX idx_fecha_creacion ON clientes(fecha_creacion);

-- Paso 4: Insertar datos de ejemplo
-- Descomentar si quieres datos de prueba
/*
INSERT INTO clientes (nombre, email, telefono, direccion) VALUES 
('Juan Pérez', 'juan@ejemplo.com', '+56 9 1234 5678', 'Calle Principal 123, Santiago'),
('María González', 'maria@ejemplo.com', '+56 9 2345 6789', 'Avenida Central 456, Santiago'),
('Carlos López', 'carlos@ejemplo.com', '+56 9 3456 7890', 'Calle Secundaria 789, Santiago'),
('Ana Martínez', 'ana@ejemplo.com', '+56 9 4567 8901', 'Paseo Norte 101, Santiago'),
('Roberto Díaz', 'roberto@ejemplo.com', '+56 9 5678 9012', 'Boulevard Sur 202, Santiago');
*/

-- ============================================================================
-- CONSULTAS ÚTILES (EJEMPLOS)
-- ============================================================================

-- Ver la estructura de la tabla
-- DESCRIBE clientes;

-- Ver todos los clientes
-- SELECT * FROM clientes;

-- Contar clientes
-- SELECT COUNT(*) as total_clientes FROM clientes;

-- Ver clientes creados hoy
-- SELECT * FROM clientes WHERE DATE(fecha_creacion) = CURDATE();

-- Ordenar por nombre
-- SELECT * FROM clientes ORDER BY nombre ASC;

-- Buscar por email
-- SELECT * FROM clientes WHERE email LIKE '%@ejemplo.com%';

-- Actualizar un cliente
-- UPDATE clientes SET telefono = '+56 9 9999 9999' WHERE id = 1;

-- Eliminar un cliente
-- DELETE FROM clientes WHERE id = 1;

-- Ver la información de la tabla
-- SHOW TABLE STATUS FROM crud_clientes_db LIKE 'clientes';

-- ============================================================================
-- NOTAS IMPORTANTES
-- ============================================================================

/*
1. CHARACTER SET utf8mb4 permite caracteres especiales (acentos, emojis)
2. COLLATE utf8mb4_unicode_ci permite búsquedas sin sensibilidad a mayúsculas
3. ENGINE=InnoDB soporta transacciones y claves foráneas
4. AUTO_INCREMENT genera IDs automáticamente
5. TIMESTAMP automáticamente registra fecha y hora
6. UNIQUE en email evita duplicados
7. NOT NULL hace que el campo sea obligatorio
8. Los índices mejoran la velocidad de búsquedas

PARA EJECUTAR ESTE ARCHIVO:
- MySQL Workbench: Click derecho en conexión → Execute SQL File
- Línea de comandos: mysql -u root -p < schema.sql
- Python: python setup_database.py
*/
