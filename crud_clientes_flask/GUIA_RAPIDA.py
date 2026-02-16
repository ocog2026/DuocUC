"""
GUÍA RÁPIDA DE INICIO - QUICK START
Para ejecutar el proyecto en 5 minutos
"""

# ============================================================================
# PASO 1: INSTALAR DEPENDENCIAS (primera vez)
# ============================================================================
"""
Abre terminal en la carpeta del proyecto y ejecuta:

    pip install -r requirements.txt

Esto instala:
- Flask (framework web)
- mysql-connector-python (conector MySQL)
"""

# ============================================================================
# PASO 2: CONFIGURAR LA BASE DE DATOS
# ============================================================================
"""
1. Edita config.py con tus credenciales MySQL:
   
   DB_HOST = 'localhost'
   DB_USER = 'root'
   DB_PASSWORD = 'tu_contraseña'  ← CAMBIAR AQUÍ
   DB_NAME = 'crud_clientes_db'
   DB_PORT = 3306

2. En terminal, ejecuta:
   
   python setup_database.py
   
   Deberías ver: ✓ BASE DE DATOS CREADA EXITOSAMENTE

3. ¡Base de datos lista! ✅
"""

# ============================================================================
# PASO 3: EJECUTAR LA APLICACIÓN
# ============================================================================
"""
En terminal, ejecuta:

    python run.py

Deberías ver algo como:

    ======================================================================
    🚀 INICIANDO APLICACIÓN FLASK - CRUD CLIENTES
    ======================================================================
    ✓ Servidor corriendo en: http://localhost:5000
    ✓ Modo DEBUG: Activado
    ======================================================================

¡Abre tu navegador en http://localhost:5000 y listo! 🎉
"""

# ============================================================================
# ARCHIVOS PRINCIPALES Y SU FUNCIÓN
# ============================================================================

archivos = {
    "config.py": {
        "Función": "Configuración de la aplicación",
        "¿Qué hacer?": "Cambiar credenciales de MySQL",
        "Editar": "Sí (al instalar)"
    },
    
    "setup_database.py": {
        "Función": "Crear la base de datos",
        "¿Qué hacer?": "Ejecutar una sola vez",
        "Comando": "python setup_database.py"
    },
    
    "run.py": {
        "Función": "Iniciar la aplicación",
        "¿Qué hacer?": "Ejecutar siempre para iniciar",
        "Comando": "python run.py"
    },
    
    "app/__init__.py": {
        "Función": "Crear la aplicación Flask",
        "¿Qué hacer?": "No tocar (código interno)",
        "Editar": "No"
    },
    
    "app/models.py": {
        "Función": "Funciones de base de datos (CRUD)",
        "¿Qué hacer?": "Leer para aprender cómo acceder a MySQL",
        "Operaciones": "INSERT, SELECT, UPDATE, DELETE"
    },
    
    "app/routes.py": {
        "Función": "Rutas (URLs) de la aplicación",
        "¿Qué hacer?": "Leer para aprender cómo conectar URLs a funciones",
        "Rutas": "/, /clientes/agregar, /clientes/editar/<id>, /clientes/eliminar/<id>"
    },
    
    "templates/base.html": {
        "Función": "Plantilla HTML base con CSS",
        "¿Qué hacer?": "Cambiar estilos aquí",
        "Elemento": "<style> contiene todos los estilos"
    },
    
    "templates/index.html": {
        "Función": "Página principal (listar clientes)",
        "¿Qué hacer?": "Leer para aprender Jinja2",
        "Conceptos": "Loops {% for %}, condicionales {% if %}"
    },
    
    "templates/agregar.html": {
        "Función": "Formulario para agregar cliente",
        "¿Qué hacer?": "Personalizar campos del formulario",
        "Elementos": "<input>, <textarea>, <form>"
    },
    
    "templates/editar.html": {
        "Función": "Formulario para editar cliente",
        "¿Qué hacer?": "Similar a agregar.html",
        "Diferencia": "Rellenado con valores actuales"
    }
}

# ============================================================================
# FLUJO DE TRABAJO
# ============================================================================

flujo = """
USUARIO ACCEDE A http://localhost:5000

        ↓
     (FLASK)
    
app.route("/")
    ↓
    └→ routes.listar_clientes()
            ↓
            └→ models.obtener_todos_clientes()
                    ↓
                    └→ get_database_connection()
                            ↓
                            └→ mysql.connector.connect()
                                    ↓
                                    └→ SELECT * FROM clientes
                    ↓
            └→ cursor.fetchall()  # Obtener resultados
                    ↓
            └→ return clientes (lista)
    ↓
    └→ render_template('index.html', clientes=clientes)
            ↓
            └→ Jinja2 renderiza el HTML
                    ↓
                    └→ HTML + CSS
                    ↓
                    └→ NAVEGADOR MUESTRA LA PÁGINA
"""

print(flujo)

# ============================================================================
# OPERACIONES CRUD
# ============================================================================

print("\n" + "="*70)
print("OPERACIONES CRUD")
print("="*70)

operaciones = {
    "CREATE (Crear)": {
        "URL": "/clientes/agregar (GET → mostrar formulario)",
        "Método HTTP": "POST",
        "Función": "routes.agregar_cliente()",
        "BD": "models.agregar_cliente()",
        "SQL": "INSERT INTO clientes (nombre, email, telefono, direccion) VALUES (...)"
    },
    
    "READ (Leer)": {
        "URL": "/ (mostrar todos) o /clientes/editar/<id> (uno específico)",
        "Método HTTP": "GET",
        "Función": "routes.listar_clientes() o routes.mostrar_formulario_editar()",
        "BD": "models.obtener_todos_clientes() o models.obtener_cliente_por_id()",
        "SQL": "SELECT * FROM clientes WHERE id = ..."
    },
    
    "UPDATE (Actualizar)": {
        "URL": "/clientes/editar/<id> (GET → mostrar, POST → guardar)",
        "Método HTTP": "POST",
        "Función": "routes.actualizar_cliente()",
        "BD": "models.actualizar_cliente()",
        "SQL": "UPDATE clientes SET nombre = ... WHERE id = ..."
    },
    
    "DELETE (Eliminar)": {
        "URL": "/clientes/eliminar/<id>",
        "Método HTTP": "POST",
        "Función": "routes.eliminar_cliente()",
        "BD": "models.eliminar_cliente()",
        "SQL": "DELETE FROM clientes WHERE id = ..."
    }
}

for operacion, detalles in operaciones.items():
    print(f"\n{operacion}:")
    for clave, valor in detalles.items():
        print(f"  {clave}: {valor}")

# ============================================================================
# VARIABLES DE ENTORNO (opcional, en producción)
# ============================================================================

print("\n" + "="*70)
print("VARIABLES DE ENTORNO (en producción)")
print("="*70)

print("""
En lugar de guardar contraseñas en config.py,
usar variables de entorno:

# Windows (PowerShell)
$env:DB_USER = "root"
$env:DB_PASSWORD = "mi_contraseña"

# Mac/Linux (Bash)
export DB_USER="root"
export DB_PASSWORD="mi_contraseña"

# Luego en config.py:
import os
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
""")

# ============================================================================
# COMANDOS ÚTILES
# ============================================================================

print("\n" + "="*70)
print("COMANDOS ÚTILES")
print("="*70)

comandos = {
    "Crear entorno virtual": "python -m venv venv",
    "Activar (Windows)": "venv\\Scripts\\activate",
    "Activar (Mac/Linux)": "source venv/bin/activate",
    "Instalar dependencias": "pip install -r requirements.txt",
    "Crear BD": "python setup_database.py",
    "Ejecutar app": "python run.py",
    "Ver versión Python": "python --version",
    "Listar paquetes": "pip list",
    "Desactivar entorno": "deactivate"
}

for comando, ejecucion in comandos.items():
    print(f"\n{comando}:")
    print(f"  $ {ejecucion}")

# ============================================================================
# VERIFICACIÓN RÁPIDA
# ============================================================================

print("\n" + "="*70)
print("CHECKLIST - ¿Está todo listo?")
print("="*70)

checklist = [
    ("Python instalado", "python --version"),
    ("pip instalado", "pip --version"),
    ("MySQL corriendo", "Abre Services en Windows o terminal en Mac/Linux"),
    ("requirements.txt", "Ver si existe en la carpeta del proyecto"),
    ("config.py editado", "Cambiar DB_USER y DB_PASSWORD"),
    ("Base de datos creada", "python setup_database.py"),
    ("Servidor Flask corriendo", "python run.py"),
    ("Navegador en localhost:5000", "Abre http://localhost:5000")
]

for i, (tarea, comando) in enumerate(checklist, 1):
    print(f"{i}. {tarea}")
    print(f"   → {comando}")
    print()
