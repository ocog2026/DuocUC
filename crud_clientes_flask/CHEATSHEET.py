"""
GUÍA VISUAL DE DÓNDE ESTÁ CADA COSA - cheatsheet.py
Referencia rápida para encontrar lo que necesitas
"""

# ════════════════════════════════════════════════════════════════════════════
# ¿DÓNDE ESTÁ? - GUÍA DE BÚSQUEDA
# ════════════════════════════════════════════════════════════════════════════

busqueda = {
    "¿Dónde cambiar la contraseña de MySQL?": {
        "Archivo": "config.py",
        "Línea": "DB_PASSWORD = 'root'  ← Cambiar aquí",
        "Sección": "CONFIGURACIÓN DE BASE DE DATOS MYSQL"
    },
    
    "¿Dónde agregar el servidor de MySQL?": {
        "Archivo": "config.py",
        "Línea": "DB_HOST = 'localhost'",
        "Sección": "CONFIGURACIÓN DE BASE DE DATOS MYSQL"
    },
    
    "¿Dónde cambiar el puerto?": {
        "Archivo": "config.py",
        "Línea": "DB_PORT = 3306",
        "Sección": "CONFIGURACIÓN DE BASE DE DATOS MYSQL"
    },
    
    "¿Dónde está la función para insertar clientes?": {
        "Archivo": "app/models.py",
        "Función": "agregar_cliente()",
        "Tipo": "CREATE"
    },
    
    "¿Dónde está la función para obtener clientes?": {
        "Archivo": "app/models.py",
        "Función": "obtener_todos_clientes()",
        "Tipo": "READ"
    },
    
    "¿Dónde está la función para editar clientes?": {
        "Archivo": "app/models.py",
        "Función": "actualizar_cliente()",
        "Tipo": "UPDATE"
    },
    
    "¿Dónde está la función para eliminar clientes?": {
        "Archivo": "app/models.py",
        "Función": "eliminar_cliente()",
        "Tipo": "DELETE"
    },
    
    "¿Dónde está la conexión a MySQL?": {
        "Archivo": "app/models.py",
        "Función": "get_database_connection()",
        "Descripción": "Crea la conexión con los datos de config.py"
    },
    
    "¿Dónde están las rutas de la aplicación?": {
        "Archivo": "app/routes.py",
        "Descripción": "Todas las funciones que procesan las URLs"
    },
    
    "¿Dónde está la ruta '/'?": {
        "Archivo": "app/routes.py",
        "Función": "listar_clientes()",
        "Descripción": "Muestra la lista de clientes"
    },
    
    "¿Dónde se crea la aplicación Flask?": {
        "Archivo": "app/__init__.py",
        "Función": "create_app()",
        "Descripción": "Factory function que crea y configura Flask"
    },
    
    "¿Dónde se inicia el servidor?": {
        "Archivo": "run.py",
        "Comando": "python run.py",
        "Puerto": "5000"
    },
    
    "¿Dónde se crea la base de datos?": {
        "Archivo": "setup_database.py",
        "Comando": "python setup_database.py",
        "Descripción": "Crea la BD y la tabla de clientes automáticamente"
    },
    
    "¿Dónde está el HTML de la página principal?": {
        "Archivo": "templates/index.html",
        "Descripción": "Tabla con lista de clientes"
    },
    
    "¿Dónde está el formulario de agregar?": {
        "Archivo": "templates/agregar.html",
        "Descripción": "Formulario para crear nuevo cliente"
    },
    
    "¿Dónde está el formulario de editar?": {
        "Archivo": "templates/editar.html",
        "Descripción": "Formulario para modificar cliente"
    },
    
    "¿Dónde están los estilos CSS?": {
        "Archivo": "templates/base.html",
        "Sección": "<style>",
        "Descripción": "Todos los estilos de la aplicación"
    },
    
    "¿Dónde está la plantilla base?": {
        "Archivo": "templates/base.html",
        "Descripción": "Heredan: index.html, agregar.html, editar.html"
    },
}

print("=" * 80)
print("¿DÓNDE ESTÁ? - GUÍA RÁPIDA DE BÚSQUEDA")
print("=" * 80)
for pregunta, respuesta in busqueda.items():
    print(f"\n❓ {pregunta}")
    for clave, valor in respuesta.items():
        print(f"   {clave}: {valor}")

# ════════════════════════════════════════════════════════════════════════════
# FLUJO DE UNA OPERACIÓN CRUD
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("FLUJO DETALLADO: CREAR UN NUEVO CLIENTE")
print("=" * 80)

flujo_crear = """
1. USUARIO ACCEDE A /clientes/agregar en navegador
   └─→ app/__init__.py: add_url_rule() recibe GET /clientes/agregar

2. FLASK EJECUTA:
   └─→ app/routes.py: mostrar_formulario_agregar()
       └─→ Retorna: render_template('agregar.html')
           └─→ templates/agregar.html se renderiza

3. USUARIO VE:
   └─→ Formulario HTML vacío con campos:
       • nombre
       • email
       • telefono
       • direccion

4. USUARIO RELLENA Y HACE CLICK "Guardar Cliente"
   └─→ Navegador envía POST /clientes/agregar
       └─→ Datos enviados: {nombre: "Juan", email: "j@...", ...}

5. FLASK EJECUTA:
   └─→ app/routes.py: agregar_cliente()
       ├─→ Obtiene datos: request.form.get('nombre'), ...
       ├─→ Valida datos (no vacíos)
       └─→ Llama: models.agregar_cliente(nombre, email, ...)

6. MODELOS EJECUTA:
   └─→ app/models.py: agregar_cliente()
       ├─→ Llama: get_database_connection()
       │   └─→ mysql.connector.connect() → conexión a MySQL
       ├─→ cursor = conexion.cursor()
       ├─→ sql = "INSERT INTO clientes (nombre, email, ...) VALUES (%s, %s, ...)"
       ├─→ cursor.execute(sql, (nombre, email, ...))
       ├─→ conexion.commit()  ← GUARDA EN LA BD
       ├─→ cursor.close()
       ├─→ conexion.close()
       └─→ return True (éxito) o False (error)

7. MYSQL GUARDA EN BD:
   └─→ INSERT INTO clientes (nombre, email, telefono, direccion)
       VALUES ('Juan', 'juan@ejemplo.com', '+56 9 1234 5678', 'Calle 123')
       
       Resultado: Nueva fila en tabla clientes:
       ┌────┬──────┬──────────────────┬──────────────┬────────────┐
       │ id │ nombre│ email            │ telefono     │ direccion  │
       ├────┼──────┼──────────────────┼──────────────┼────────────┤
       │ 1  │ Juan │ juan@ejemplo.com │ +56 9 1234.. │ Calle 123  │
       └────┴──────┴──────────────────┴──────────────┴────────────┘

8. VUELVE A app/routes.py: agregar_cliente()
   └─→ if models.agregar_cliente(...):
           ├─→ flash('✓ Cliente agregado exitosamente')
           └─→ return redirect(url_for('listar_clientes'))

9. NAVEGADOR RECIBE REDIRECCIÓN:
   └─→ GET / (redirecciona a listar_clientes)

10. FLASK EJECUTA:
    └─→ app/routes.py: listar_clientes()
        ├─→ clientes = models.obtener_todos_clientes()
        │   └─→ SELECT * FROM clientes (obtiene todos incluyendo el nuevo)
        └─→ render_template('index.html', clientes=clientes)

11. USUARIO VE:
    └─→ Tabla con todos los clientes (incluyendo el nuevo "Juan")
    └─→ Mensaje: "✓ Cliente agregado exitosamente"
"""

print(flujo_crear)

# ════════════════════════════════════════════════════════════════════════════
# MATRIZ DE RUTAS
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("MATRIZ DE RUTAS Y FUNCIONES")
print("=" * 80)

print("""
┌──────────────────────┬────────┬──────────────────────────┬──────────────────────┐
│ RUTA                 │ MÉTODO │ FUNCIÓN (routes.py)      │ FUNCIÓN (models.py)  │
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /                    │ GET    │ listar_clientes()        │ obtener_todos_clientes()
│                      │        │                          │ get_database_connection()
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /clientes/agregar    │ GET    │ mostrar_formulario_      │ (ninguna)
│                      │        │ agregar()                │ Muestra formulario vacío
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /clientes/agregar    │ POST   │ agregar_cliente()        │ agregar_cliente()
│                      │        │                          │ get_database_connection()
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /clientes/editar/<id>│ GET    │ mostrar_formulario_      │ obtener_cliente_por_id()
│                      │        │ editar()                 │ get_database_connection()
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /clientes/editar/<id>│ POST   │ actualizar_cliente()     │ actualizar_cliente()
│                      │        │                          │ get_database_connection()
├──────────────────────┼────────┼──────────────────────────┼──────────────────────┤
│ /clientes/eliminar   │ POST   │ eliminar_cliente()       │ eliminar_cliente()
│ /<id>                │        │                          │ get_database_connection()
└──────────────────────┴────────┴──────────────────────────┴──────────────────────┘
""")

# ════════════════════════════════════════════════════════════════════════════
# CICLO DE VIDA DE UNA SOLICITUD HTTP
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("CICLO DE VIDA DE UNA SOLICITUD HTTP EN FLASK")
print("=" * 80)

ciclo = """
1. USUARIO ABRE NAVEGADOR
   └─→ Escribe: http://localhost:5000

2. NAVEGADOR ENVÍA SOLICITUD HTTP
   └─→ GET / HTTP/1.1
       Host: localhost:5000
       Connection: keep-alive
       ...

3. SERVIDOR FLASK RECIBE SOLICITUD
   └─→ En run.py: app.run()
       └─→ Puerto 5000 escucha y recibe

4. FLASK ANALIZA LA URL
   └─→ ¿Es la ruta "/" registrada?
   └─→ ¿Es GET o POST?
   └─→ ¿Hay parámetros dinámicos?

5. FLASK BUSCA LA RUTA COINCIDENTE
   └─→ En app/__init__.py: app.add_url_rule()
   └─→ Encuentra: "/" → routes.listar_clientes()

6. FLASK EJECUTA LA FUNCIÓN
   └─→ routes.listar_clientes()
       ├─→ Llama a models.obtener_todos_clientes()
       │   └─→ Se conecta a MySQL
       │   └─→ SELECT * FROM clientes
       │   └─→ Retorna lista de clientes
       ├─→ Pasa datos a template: render_template('index.html', clientes=clientes)
       └─→ Jinja2 renderiza HTML con los datos

7. JINJA2 PROCESA EL TEMPLATE
   └─→ Lee templates/index.html
   └─→ Procesa variables: {{ cliente['nombre'] }}
   └─→ Procesa bucles: {% for cliente in clientes %}
   └─→ Procesa condicionales: {% if clientes %}
   └─→ Genera HTML final

8. FLASK RESPONDE AL NAVEGADOR
   └─→ HTTP/1.1 200 OK
       Content-Type: text/html; charset=utf-8
       Content-Length: 5432
       
       <!DOCTYPE html>
       <html>
       <head>
           <title>CRUD Clientes</title>
           ...
       </head>
       <body>
           <table>
               <tr>
                   <td>1</td>
                   <td>Juan Pérez</td>
                   ...

9. NAVEGADOR RECIBE RESPUESTA HTML
   └─→ Descarga el HTML
   └─→ Descarga recursos: CSS, imágenes, JS
   └─→ Renderiza la página

10. USUARIO VE LA PÁGINA
    └─→ Tabla de clientes
    └─→ Botones Editar/Eliminar
    └─→ Botón Agregar nuevo cliente
"""

print(ciclo)

# ════════════════════════════════════════════════════════════════════════════
# TIPOS DE DATOS IMPORTANTES
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("TIPOS DE DATOS EN PYTHON Y MYSQL")
print("=" * 80)

tipos = """
PYTHON                  ↔  MYSQL              ↔  HTML
─────────────────────────────────────────────────────────────
str (texto)             ↔  VARCHAR, TEXT      ↔  input type="text"
int (número)            ↔  INT                ↔  input type="number"
float (decimal)         ↔  FLOAT, DECIMAL     ↔  input type="number"
bool (verdadero/falso)  ↔  BOOL, INT          ↔  input type="checkbox"
dict (diccionario)      ↔  No directo         ↔  JSON
list (lista)            ↔  No directo         ↔  JSON array
datetime (fecha/hora)   ↔  DATETIME,          ↔  input type="datetime"
                            TIMESTAMP

EJEMPLOS:
─────────────────────────────────────────────────────────────

Python:
    cliente = {
        'id': 1,                              # int
        'nombre': 'Juan',                     # str
        'email': 'juan@ejemplo.com',          # str
        'telefono': '+56912345678',           # str
        'direccion': 'Calle 123',             # str
        'fecha_creacion': '2024-01-15 10:30:00'  # datetime
    }

MySQL:
    CREATE TABLE clientes (
        id INT,                           -- int
        nombre VARCHAR(100),              -- str
        email VARCHAR(100),               -- str
        telefono VARCHAR(20),             -- str
        direccion TEXT,                   -- str
        fecha_creacion TIMESTAMP          -- datetime
    );

HTML:
    <form>
        <input type="text" name="nombre">          <!-- str -->
        <input type="email" name="email">          <!-- str -->
        <input type="tel" name="telefono">         <!-- str -->
        <textarea name="direccion"></textarea>     <!-- str -->
    </form>
"""

print(tipos)

# ════════════════════════════════════════════════════════════════════════════
# CHECKLIST DE INSTALACIÓN
# ════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("CHECKLIST DE INSTALACIÓN")
print("=" * 80)

checklist = """
□ Python 3.8+ instalado
  └─ Verificar: python --version

□ pip instalado
  └─ Verificar: pip --version

□ MySQL instalado y corriendo
  └─ Verificar: mysql --version
  └─ Servidor: Debería estar corriendo en puerto 3306

□ Carpeta del proyecto creada
  └─ crud_clientes_flask/

□ requirements.txt existe
  └─ pip install -r requirements.txt

□ config.py editado con credenciales
  └─ DB_USER, DB_PASSWORD

□ setup_database.py ejecutado
  └─ python setup_database.py
  └─ Ver mensaje: ✓ BASE DE DATOS CREADA EXITOSAMENTE

□ Entorno virtual (opcional pero recomendado)
  └─ python -m venv venv
  └─ venv\\Scripts\\activate (Windows)
  └─ source venv/bin/activate (Mac/Linux)

□ Aplicación Flask iniciada
  └─ python run.py
  └─ Ver mensaje: ✓ Servidor corriendo en: http://localhost:5000

□ Navegador abierto
  └─ http://localhost:5000
  └─ Ver tabla de clientes

✅ ¡LISTO! La aplicación está funcionando
"""

print(checklist)

print("\n" + "=" * 80)
print("Fin del cheatsheet")
print("=" * 80)
