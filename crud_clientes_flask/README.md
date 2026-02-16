# CRUD Clientes con MySQL, Python y Flask

## 📚 Descripción del Proyecto

Este proyecto es una **aplicación CRUD educativa** (Create, Read, Update, Delete) para gestionar clientes. 
Está diseñada para aprender cómo integrar:
- **Python**: Lenguaje de programación
- **Flask**: Framework web
- **MySQL**: Base de datos
- **HTML/CSS**: Interfaz de usuario

---

## 🎯 ¿Qué es CRUD?

**CRUD** son las 4 operaciones básicas en base de datos:

| Operación | Descripción | SQL | HTTP |
|-----------|-------------|-----|------|
| **C**reate | Crear nuevos registros | INSERT | POST |
| **R**ead | Leer/consultar registros | SELECT | GET |
| **U**pdate | Modificar registros existentes | UPDATE | POST/PUT |
| **D**elete | Eliminar registros | DELETE | POST/DELETE |

---

## 📁 Estructura del Proyecto

```
crud_clientes_flask/
│
├── config.py                    # ⚙️ Configuración de la aplicación
├── run.py                       # 🚀 Archivo principal (ejecutar con python run.py)
├── setup_database.py            # 🗄️ Script para crear la BD
├── requirements.txt             # 📦 Dependencias del proyecto
├── README.md                    # 📖 Este archivo
│
├── app/
│   ├── __init__.py             # 🏭 Factory function de Flask
│   ├── models.py               # 📊 Funciones de base de datos
│   └── routes.py               # 🛣️ Rutas y vistas
│
└── templates/
    ├── base.html               # 🎨 Plantilla base (CSS y estructura)
    ├── index.html              # 📋 Página principal (listar clientes)
    ├── agregar.html            # ➕ Formulario para agregar
    └── editar.html             # ✎ Formulario para editar
```

---

## 🔧 Requisitos Previos

Antes de empezar, necesitas tener instalado:

1. **Python 3.8+**
   - Descarga desde: https://www.python.org/downloads/
   - Verifica: `python --version`

2. **MySQL Server**
   - Descarga desde: https://dev.mysql.com/downloads/mysql/
   - Verifica: `mysql --version`

3. **pip** (gestor de paquetes Python)
   - Generalmente viene incluido con Python
   - Verifica: `pip --version`

---

## 📦 Instalación Paso a Paso

### Paso 1: Clonar o descargar el proyecto

```bash
# Si tienes git:
git clone <url-del-proyecto>

# O simplemente asegúrate de tener todos los archivos en una carpeta
```

### Paso 2: Abrir terminal en la carpeta del proyecto

```bash
# En Windows:
# 1. Click derecho en la carpeta → "Abrir terminal aquí"
# 2. O navega con: cd C:\ruta\a\la\carpeta

# En Mac/Linux:
cd /ruta/a/la/carpeta
```

### Paso 3: Crear un entorno virtual (recomendado)

Un **entorno virtual** mantiene las dependencias del proyecto aisladas.

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno (Windows)
venv\Scripts\activate

# Activar el entorno (Mac/Linux)
source venv/bin/activate

# Deberías ver "(venv)" al inicio de la línea en la terminal
```

### Paso 4: Instalar dependencias

```bash
pip install -r requirements.txt
```

Las dependencias que se instalarán son:
- **Flask**: Framework web
- **mysql-connector-python**: Conector para MySQL

### Paso 5: Configurar la base de datos

Edita el archivo `config.py` con tus credenciales de MySQL:

```python
DB_HOST = 'localhost'        # Host de MySQL
DB_USER = 'root'            # Usuario MySQL
DB_PASSWORD = 'tu_contraseña'  # Tu contraseña
DB_NAME = 'crud_clientes_db' # Nombre de la BD
DB_PORT = 3306              # Puerto MySQL
```

### Paso 6: Crear la base de datos

Ejecuta el script de configuración:

```bash
python setup_database.py
```

Deberías ver:
```
======================================================================
✓ BASE DE DATOS CREADA EXITOSAMENTE
======================================================================
```

---

## 🚀 Ejecutar la Aplicación

```bash
# Asegúrate de que el entorno virtual esté activado (ver Paso 3)

# Ejecutar la aplicación
python run.py
```

Deberías ver:
```
======================================================================
🚀 INICIANDO APLICACIÓN FLASK - CRUD CLIENTES
======================================================================
✓ Servidor corriendo en: http://localhost:5000
✓ Modo DEBUG: Activado (reinicio automático de cambios)
✓ Presiona CTRL+C para detener el servidor
======================================================================
```

---

## 🌐 Acceder a la Aplicación

Abre tu navegador web en:

```
http://localhost:5000
```

¡Deberías ver la interfaz de la aplicación CRUD!

---

## 📱 Funciones Principales

### 1. **Listar Clientes** (READ)
- **URL**: `/`
- **Método**: GET
- **Descripción**: Muestra todos los clientes en una tabla
- **Archivos relacionados**: `index.html`, `models.obtener_todos_clientes()`

### 2. **Agregar Cliente** (CREATE)
- **URL**: `/clientes/agregar`
- **Método**: GET (mostrar formulario) / POST (guardar)
- **Descripción**: Crea un nuevo cliente
- **Archivos relacionados**: `agregar.html`, `models.agregar_cliente()`

### 3. **Editar Cliente** (UPDATE)
- **URL**: `/clientes/editar/<id>`
- **Método**: GET (mostrar formulario) / POST (guardar cambios)
- **Descripción**: Modifica un cliente existente
- **Archivos relacionados**: `editar.html`, `models.actualizar_cliente()`

### 4. **Eliminar Cliente** (DELETE)
- **URL**: `/clientes/eliminar/<id>`
- **Método**: POST
- **Descripción**: Elimina un cliente de la BD
- **Archivos relacionados**: `models.eliminar_cliente()`

---

## 🎓 Flujo de Ejecución

### Cuando abres http://localhost:5000

```
1. Se acciona la ruta "/"
   ↓
2. Se ejecuta función listar_clientes() (en routes.py)
   ↓
3. Se llama a models.obtener_todos_clientes()
   ↓
4. models.py se conecta a MySQL con get_database_connection()
   ↓
5. Se ejecuta: SELECT * FROM clientes
   ↓
6. Los resultados se pasan al template index.html
   ↓
7. index.html renderiza la tabla HTML con los datos
   ↓
8. El navegador muestra la página
```

### Cuando das click en "Agregar Cliente"

```
1. Se acciona GET /clientes/agregar
   ↓
2. Se ejecuta mostrar_formulario_agregar() → Muestra agregar.html
   ↓
3. Completas el formulario
   ↓
4. Haces click en "Guardar Cliente"
   ↓
5. Se envía POST /clientes/agregar
   ↓
6. Se ejecuta agregar_cliente() (routes.py)
   ↓
7. Se llama a models.agregar_cliente()
   ↓
8. Se ejecuta: INSERT INTO clientes VALUES (...)
   ↓
9. Se guarda (COMMIT) en MySQL
   ↓
10. Se muestra mensaje de éxito
   ↓
11. Redirecciona a / (lista de clientes)
```

---

## 📊 Estructura de la Base de Datos

Tabla: **clientes**

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | INT (PK, Auto) | ID único del cliente |
| `nombre` | VARCHAR(100) | Nombre del cliente |
| `email` | VARCHAR(100) | Email único del cliente |
| `telefono` | VARCHAR(20) | Teléfono del cliente |
| `direccion` | TEXT | Dirección del cliente |
| `fecha_creacion` | TIMESTAMP | Fecha de creación automática |
| `fecha_actualizacion` | TIMESTAMP | Fecha de última actualización |

---

## 🐛 Solucionar Problemas

### ❌ "Error: No se puede conectar a MySQL"

**Solución:**
1. Verifica que MySQL esté corriendo
2. En Windows: Services → Busca "MySQL" → Click derecho → "Start"
3. Verifica usuario y contraseña en `config.py`
4. Verifica el puerto (por defecto 3306)

### ❌ "ModuleNotFoundError: No module named 'mysql'"

**Solución:**
```bash
pip install mysql-connector-python
```

### ❌ "ModuleNotFoundError: No module named 'flask'"

**Solución:**
```bash
pip install Flask
```

### ❌ La página no carga / Error 404

**Solución:**
1. Verifica que el servidor esté corriendo (deberías ver el mensaje en la terminal)
2. Verifica que accedas a `http://localhost:5000` (no olvides el puerto)
3. Presiona Ctrl+C y reinicia `python run.py`

---

## 💡 Conceptos Clave para Aprender

### 1. **Conexión a BD**
```python
# Ver en: app/models.py → get_database_connection()
conexion = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)
```

### 2. **Consultas SQL**
```python
# INSERT - Crear
cursor.execute("INSERT INTO clientes (nombre, email) VALUES (%s, %s)", (nombre, email))

# SELECT - Leer
cursor.execute("SELECT * FROM clientes")

# UPDATE - Actualizar
cursor.execute("UPDATE clientes SET nombre = %s WHERE id = %s", (nombre, id))

# DELETE - Eliminar
cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))

# COMMIT - Guardar cambios
conexion.commit()
```

### 3. **Rutas Flask**
```python
# Ver en: app/__init__.py
app.add_url_rule('/ruta', 'nombre', funcion, methods=['GET', 'POST'])
```

### 4. **Templates Jinja2**
```html
<!-- Loops -->
{% for cliente in clientes %}
    {{ cliente['nombre'] }}
{% endfor %}

<!-- Condicionales -->
{% if clientes %}
    Hay clientes
{% else %}
    No hay clientes
{% endif %}

<!-- Variables -->
{{ variable }}
```

---

## 🚀 Mejoras Futuras

Puedes extender este proyecto agregando:

- ✅ Autenticación de usuarios (login/logout)
- ✅ Búsqueda y filtrado de clientes
- ✅ Paginación de resultados
- ✅ Exportar a CSV/Excel
- ✅ Gráficos y reportes
- ✅ Validación más robusta
- ✅ API REST (con Flask-RESTful)
- ✅ Testing (pytest)
- ✅ Despliegue en servidor (Heroku, AWS, etc.)

---

## 📚 Recursos Adicionales

- **Documentación Flask**: https://flask.palletsprojects.com/
- **Documentación MySQL**: https://dev.mysql.com/doc/
- **Tutorial Python**: https://python.readthedocs.io/
- **HTML/CSS**: https://developer.mozilla.org/es/docs/Web/

---

## ✍️ Autor

Proyecto educativo - Fundamentos de Programación

---

## 📝 Notas Importantes

- El archivo `config.py` contiene credenciales. ⚠️ **No compartir** en repositorios públicos.
- En producción, usar variables de entorno para las credenciales.
- Verificar que `requirements.txt` esté actualizado antes de compartir.

---

**¡Felicidades! Ahora entiendes cómo funciona un CRUD con Flask y MySQL! 🎉**
