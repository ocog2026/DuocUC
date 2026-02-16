"""
EJEMPLOS DE CÓDIGO - Como aprender programando
Este archivo contiene ejemplos prácticos de cada concepto usado en el proyecto
"""

# ============================================================================
# EJEMPLO 1: CONEXIÓN A MYSQL
# ============================================================================

# Código en: app/models.py → get_database_connection()

print("=" * 70)
print("EJEMPLO 1: Conectar a MySQL")
print("=" * 70)

codigo_conexion = """
import mysql.connector
import config

# Crear la conexión
conexion = mysql.connector.connect(
    host=config.DB_HOST,        # 'localhost'
    user=config.DB_USER,        # 'root'
    password=config.DB_PASSWORD,# 'contraseña'
    database=config.DB_NAME,    # 'crud_clientes_db'
    port=config.DB_PORT         # 3306
)

# Verificar si fue exitosa
if conexion.is_connected():
    print("✓ Conectado a MySQL")
else:
    print("✗ Error en conexión")
"""

print(codigo_conexion)

# ============================================================================
# EJEMPLO 2: OPERACIÓN INSERT (CREAR)
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 2: Insertar un nuevo cliente (CREATE)")
print("=" * 70)

codigo_insert = """
# Obtener la conexión
conexion = get_database_connection()

# Crear un cursor (objeto para ejecutar SQL)
cursor = conexion.cursor()

# Escribir la consulta SQL
sql = \"\"\"
INSERT INTO clientes (nombre, email, telefono, direccion)
VALUES (%s, %s, %s, %s)
\"\"\"

# Datos del nuevo cliente
datos = ('Juan Pérez', 'juan@ejemplo.com', '+56 9 1234 5678', 'Calle Principal 123')

# Ejecutar la consulta con los datos
cursor.execute(sql, datos)

# Guardar los cambios (COMMIT)
conexion.commit()

# Cerrar conexión
cursor.close()
conexion.close()

print(f"✓ Se insertó 1 cliente nuevo")
"""

print(codigo_insert)

# ============================================================================
# EJEMPLO 3: OPERACIÓN SELECT (LEER)
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 3: Obtener todos los clientes (READ)")
print("=" * 70)

codigo_select = """
# Obtener conexión
conexion = get_database_connection()

# Crear cursor con dictionary=True para obtener diccionarios
cursor = conexion.cursor(dictionary=True)

# Escribir consulta SELECT
sql = \"SELECT * FROM clientes ORDER BY fecha_creacion DESC\"

# Ejecutar
cursor.execute(sql)

# Obtener todos los resultados
clientes = cursor.fetchall()  # fetchall() retorna una lista de diccionarios

# Procesar resultados
for cliente in clientes:
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Email: {cliente['email']}")
    print(f"Teléfono: {cliente['telefono']}")
    print(f"Dirección: {cliente['direccion']}")
    print("---")

# Cerrar
cursor.close()
conexion.close()
"""

print(codigo_select)

# ============================================================================
# EJEMPLO 4: OPERACIÓN UPDATE (ACTUALIZAR)
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 4: Actualizar un cliente (UPDATE)")
print("=" * 70)

codigo_update = """
# Obtener conexión
conexion = get_database_connection()
cursor = conexion.cursor()

# Consulta UPDATE
sql = \"\"\"
UPDATE clientes 
SET nombre = %s, email = %s, telefono = %s, direccion = %s 
WHERE id = %s
\"\"\"

# Datos nuevos (el último es el ID del cliente a actualizar)
datos = ('Juan Pérez Actualizado', 'nuevo@ejemplo.com', '+56 9 9999 9999', 'Nueva dirección 999', 1)

# Ejecutar
cursor.execute(sql, datos)

# Guardar cambios
conexion.commit()

# Verificar cuántas filas fueron afectadas
filas_afectadas = cursor.rowcount
print(f"✓ Se actualizaron {filas_afectadas} cliente(s)")

cursor.close()
conexion.close()
"""

print(codigo_update)

# ============================================================================
# EJEMPLO 5: OPERACIÓN DELETE (ELIMINAR)
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 5: Eliminar un cliente (DELETE)")
print("=" * 70)

codigo_delete = """
# Obtener conexión
conexion = get_database_connection()
cursor = conexion.cursor()

# Consulta DELETE
sql = \"DELETE FROM clientes WHERE id = %s\"

# El ID del cliente a eliminar
cliente_id = 1

# Ejecutar
cursor.execute(sql, (cliente_id,))

# Guardar cambios
conexion.commit()

# Verificar
filas_afectadas = cursor.rowcount
if filas_afectadas > 0:
    print(f"✓ Cliente eliminado exitosamente")
else:
    print(f"✗ No se encontró cliente con ID {cliente_id}")

cursor.close()
conexion.close()
"""

print(codigo_delete)

# ============================================================================
# EJEMPLO 6: RUTAS FLASK
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 6: Definir rutas en Flask")
print("=" * 70)

codigo_rutas = """
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# RUTA GET - Mostrar página
@app.route('/')
def index():
    clientes = models.obtener_todos_clientes()
    return render_template('index.html', clientes=clientes)

# RUTA GET/POST - Mostrar formulario (GET) o procesar (POST)
@app.route('/clientes/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    if request.method == 'GET':
        # Mostrar el formulario
        return render_template('agregar.html')
    
    elif request.method == 'POST':
        # Procesar el formulario enviado
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        
        # Insertar en BD
        models.agregar_cliente(nombre, email, telefono, direccion)
        
        # Redireccionar a la lista
        return redirect(url_for('index'))

# RUTA CON PARÁMETRO DINÁMICO
@app.route('/clientes/editar/<int:cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    if request.method == 'GET':
        cliente = models.obtener_cliente_por_id(cliente_id)
        return render_template('editar.html', cliente=cliente)
    
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        
        models.actualizar_cliente(cliente_id, nombre, email, telefono, direccion)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
"""

print(codigo_rutas)

# ============================================================================
# EJEMPLO 7: TEMPLATES JINJA2
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 7: Usar Jinja2 en templates")
print("=" * 70)

codigo_templates = """
<!-- Mostrar una variable -->
<h1>{{ titulo }}</h1>
<p>Bienvenido, {{ usuario }}</p>

<!-- Bucle FOR -->
{% for cliente in clientes %}
    <div>
        <h3>{{ cliente['nombre'] }}</h3>
        <p>Email: {{ cliente['email'] }}</p>
        <p>Teléfono: {{ cliente['telefono'] }}</p>
    </div>
{% endfor %}

<!-- Condicional IF -->
{% if clientes %}
    <p>Hay {{ clientes|length }} clientes</p>
{% else %}
    <p>No hay clientes</p>
{% endif %}

<!-- Generar URLs con url_for -->
<a href="{{ url_for('index') }}">Ir al inicio</a>
<a href="{{ url_for('mostrar_formulario_editar', cliente_id=5) }}">Editar cliente 5</a>

<!-- Formulario -->
<form method=\"POST\" action=\"{{ url_for('agregar_cliente') }}\">
    <input type=\"text\" name=\"nombre\" required>
    <input type=\"email\" name=\"email\" required>
    <button type=\"submit\">Guardar</button>
</form>

<!-- Mostrar mensajes flash -->
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <div class=\"alert\">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}

<!-- Herencia de templates -->
{% extends \"base.html\" %}
{% block content %}
    Contenido específico de esta página
{% endblock %}
"""

print(codigo_templates)

# ============================================================================
# EJEMPLO 8: CICLO COMPLETO - FORMULARIO USUARIO
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 8: Ciclo completo - Agregar cliente")
print("=" * 70)

ciclo_completo = """
┌─────────────────────────────────────────────────────────────┐
│ USUARIO COMPLETA FORMULARIO Y HACE CLICK EN GUARDAR        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ NAVEGADOR ENVÍA POST /clientes/agregar                     │
│ CON DATOS:                                                  │
│   - nombre: "Juan Pérez"                                    │
│   - email: "juan@ejemplo.com"                               │
│   - telefono: "+56 9 1234 5678"                             │
│   - direccion: "Calle Principal 123"                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ FLASK RECIBE POST y EJECUTA:                                │
│   agregar_cliente() en routes.py                            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ routes.agregar_cliente() OBTIENE LOS DATOS:                 │
│   nombre = request.form.get('nombre')                       │
│   email = request.form.get('email')                         │
│   telefono = request.form.get('telefono')                   │
│   direccion = request.form.get('direccion')                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ VALIDA LOS DATOS                                            │
│   if not nombre or not email or ...:                        │
│       flash('Error: campos vacíos')                         │
│       return redirect(...)                                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ LLAMA A models.agregar_cliente(...)                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ models.agregar_cliente() REALIZA:                           │
│   1. get_database_connection() → conecta a MySQL            │
│   2. cursor = conexion.cursor()                             │
│   3. cursor.execute(sql, (nombre, email, ...))              │
│   4. conexion.commit()  ← GUARDA EN LA BD                   │
│   5. cursor.close(), conexion.close()                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ RETORNA A routes.agregar_cliente()                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ MUESTRA MENSAJE DE ÉXITO                                    │
│   flash('✓ Cliente agregado exitosamente')                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ REDIRECCIONA A /                                            │
│   return redirect(url_for('listar_clientes'))               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ NAVEGADOR RECIBE REDIRECCIÓN y ACCEDE A /                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ SE EJECUTA listar_clientes() nuevamente                     │
│   (ahora con el nuevo cliente en la BD)                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ USUARIO VE LA TABLA CON EL NUEVO CLIENTE AGREGADO           │
└─────────────────────────────────────────────────────────────┘
"""

print(ciclo_completo)

# ============================================================================
# EJEMPLO 9: SQL JOIN (Avanzado)
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 9: Consultas más avanzadas (Bonus)")
print("=" * 70)

codigo_avanzado = """
-- Buscar por nombre (LIKE busca similitud)
SELECT * FROM clientes 
WHERE nombre LIKE '%Juan%';

-- Buscar por dominio de email
SELECT * FROM clientes 
WHERE email LIKE '%@gmail.com';

-- Ordenar por nombre alfabéticamente
SELECT * FROM clientes 
ORDER BY nombre ASC;

-- Ordenar por fecha (más recientes primero)
SELECT * FROM clientes 
ORDER BY fecha_creacion DESC;

-- Filtrar por fecha de creación (últimos 30 días)
SELECT * FROM clientes 
WHERE fecha_creacion >= DATE_SUB(NOW(), INTERVAL 30 DAY);

-- Contar clientes por letra inicial
SELECT 
    LEFT(nombre, 1) as primera_letra,
    COUNT(*) as cantidad
FROM clientes
GROUP BY LEFT(nombre, 1)
ORDER BY primera_letra;

-- Paginación (mostrar 10 por página)
SELECT * FROM clientes 
LIMIT 10 OFFSET 0;  -- Página 1
-- OFFSET 10 para página 2, OFFSET 20 para página 3, etc.

-- Búsqueda con múltiples condiciones
SELECT * FROM clientes 
WHERE (nombre LIKE '%Juan%' OR nombre LIKE '%María%')
AND DATE(fecha_creacion) = CURDATE();

-- Actualizar múltiples registros
UPDATE clientes 
SET telefono = '+56 9 0000 0000' 
WHERE email LIKE '%@outlook.com';

-- Eliminar con condición
DELETE FROM clientes 
WHERE fecha_creacion < DATE_SUB(NOW(), INTERVAL 1 YEAR);
"""

print(codigo_avanzado)

# ============================================================================
# EJEMPLO 10: MANEJO DE ERRORES
# ============================================================================

print("\n" + "=" * 70)
print("EJEMPLO 10: Manejo de errores Try/Except")
print("=" * 70)

codigo_errores = """
try:
    # Código que podría generar error
    conexion = get_database_connection()
    if not conexion:
        print("✗ No se puede conectar a MySQL")
        return False
    
    cursor = conexion.cursor()
    sql = "INSERT INTO clientes (nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s)"
    datos = (nombre, email, telefono, direccion)
    cursor.execute(sql, datos)
    conexion.commit()
    
    print(f"✓ Cliente agregado exitosamente")
    return True
    
except Error as e:
    # Si ocurre error, ejecutar este código
    print(f"✗ Error en la base de datos: {e}")
    return False
    
except Exception as e:
    # Captura otros errores inesperados
    print(f"✗ Error inesperado: {e}")
    return False
    
finally:
    # Siempre ejecutar esto (limpieza)
    cursor.close()
    conexion.close()
    print("✓ Conexión cerrada")
"""

print(codigo_errores)

# ============================================================================
# RESUMEN FINAL
# ============================================================================

print("\n" + "=" * 70)
print("RESUMEN DE CONCEPTOS CLAVE")
print("=" * 70)

resumen = """
✅ CONCEPTOS APRENDIDOS:

1. CONEXIÓN A BASE DE DATOS
   - mysql.connector.connect()
   - Credenciales de conexión
   - Manejo de errores

2. OPERACIONES CRUD
   - CREATE: INSERT (agregar nuevos datos)
   - READ: SELECT (obtener datos)
   - UPDATE: UPDATE (modificar datos)
   - DELETE: DELETE (eliminar datos)

3. CONSULTAS SQL
   - Parámetros con %s (protección SQL injection)
   - WHERE para filtrar
   - ORDER BY para ordenar
   - LIMIT para limitar resultados

4. FRAMEWORK FLASK
   - Rutas: @app.route()
   - GET vs POST
   - Parámetros dinámicos en URLs
   - Renderizado de templates

5. TEMPLATES JINJA2
   - Variables: {{ variable }}
   - Bucles: {% for item in items %}
   - Condicionales: {% if condición %}
   - Herencia: {% extends "base.html" %}

6. HTML FORMS
   - Métodos GET y POST
   - Inputs, textareas, botones
   - Nombres de campos (name attribute)
   - Validación con required

7. MANEJO DE ERRORES
   - Try/Except para capturar errores
   - Finally para limpiar recursos
   - Mensajes de error al usuario

8. SEGURIDAD
   - SQL Injection prevention (usar %s)
   - Validación de entrada
   - Contraseñas no en código (variables de entorno)
"""

print(resumen)
