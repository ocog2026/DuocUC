# Paso 1: Importar módulos necesarios de Flask
# - Flask: Clase principal para crear la aplicación web.
# - request: Objeto para acceder a datos de solicitudes HTTP (ej. formularios).
from flask import Flask, request

# Paso 2: Crear la instancia de la aplicación Flask
# - __name__: Variable que indica el nombre del módulo actual (usado por Flask para rutas y configuraciones).
# - Esto inicializa la app con configuración predeterminada.
app = Flask(__name__)

# Paso 3: Definir una ruta GET para la página principal
# - @app.route("/"): Decorador que registra la función para la URL raíz (/).
# - Solo acepta GET por defecto.
@app.route("/")
def hello_world():
    # Retorna una respuesta HTML simple.
    return "<p>Hello, World!</p>"

# Paso 4: Definir una ruta que maneja GET y POST
# - methods=["GET", "POST"]: Especifica que la ruta acepta ambos métodos HTTP.
# - Para GET: Muestra un formulario.
# - Para POST: Procesa los datos enviados.
@app.route("/submit", methods=["GET", "POST"])
def submit():
    # Verificar si la solicitud es POST (datos enviados desde el formulario).
    if request.method == "POST":
        # Extraer el valor del campo 'name' del formulario.
        name = request.form.get("name")  # Obtiene el dato del formulario
        # Retornar una respuesta personalizada con el nombre.
        return f"<p>Hola, {name}!</p>"  # Respuesta personalizada
    # Si es GET, mostrar el formulario HTML.
    # Si es GET, muestra el formulario
    return '''
    <form method="POST">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Enviar</button>
    </form>
    '''

# Paso 5: Ejecutar la aplicación si el script se corre directamente
# - if __name__ == '__main__': Asegura que el servidor solo inicie si no se importa como módulo.
# - app.run(debug=True): Inicia el servidor de desarrollo con modo debug (recarga automática, errores detallados).
if __name__ == '__main__':
    app.run(debug=True)