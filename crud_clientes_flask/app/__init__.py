"""
INICIALIZADOR DE LA APLICACIÓN FLASK - app/__init__.py
Este archivo inicializa la aplicación Flask y registra las rutas.

PASO 4: Crear la aplicación Flask y registrar las rutas
"""

from flask import Flask
from . import routes


def create_app():
    """
    Factory function para crear la aplicación Flask.
    
    EXPLICACIÓN:
    - Crea la instancia de Flask
    - Registra las rutas (vistas)
    - Configura opciones básicas
    
    RETORNA:
    - app: La aplicación Flask configurada
    """
    # Crear la aplicación Flask
    # __name__ es el nombre del paquete (app)
    app = Flask(__name__)
    
    # ========================================================================
    # REGISTRAR LAS RUTAS
    # ========================================================================
    # add_url_rule() conecta una URL con una función
    # Sintaxis: add_url_rule(url, endpoint, view_func, methods=['GET', 'POST'])
    
    # RUTA 1: Listar todos los clientes
    # GET / → mostrar lista
    app.add_url_rule(
        '/',  # URL raíz
        'listar_clientes',  # nombre de la ruta (endpoint)
        routes.listar_clientes,  # función a ejecutar
        methods=['GET']  # método HTTP permitido
    )
    
    # RUTA 2: Mostrar formulario para agregar
    # GET /clientes/agregar → mostrar formulario vacío
    app.add_url_rule(
        '/clientes/agregar',
        'agregar_cliente_form',
        routes.mostrar_formulario_agregar,
        methods=['GET']
    )
    
    # RUTA 3: Procesar formulario de agregar
    # POST /clientes/agregar → insertar cliente
    app.add_url_rule(
        '/clientes/agregar',
        'agregar_cliente_post',
        routes.agregar_cliente,
        methods=['POST']
    )
    
    # RUTA 4: Mostrar formulario para editar
    # GET /clientes/editar/<cliente_id> → mostrar formulario rellenado
    app.add_url_rule(
        '/clientes/editar/<int:cliente_id>',
        'mostrar_formulario_editar',
        routes.mostrar_formulario_editar,
        methods=['GET']
    )
    
    # RUTA 5: Procesar formulario de editar
    # POST /clientes/editar/<cliente_id> → actualizar cliente
    app.add_url_rule(
        '/clientes/editar/<int:cliente_id>',
        'actualizar_cliente_post',
        routes.actualizar_cliente,
        methods=['POST']
    )
    
    # RUTA 6: Eliminar cliente
    # POST /clientes/eliminar/<cliente_id> → eliminar cliente
    app.add_url_rule(
        '/clientes/eliminar/<int:cliente_id>',
        'eliminar_cliente',
        routes.eliminar_cliente,
        methods=['POST']
    )
    
    # ========================================================================
    # CONFIGURACIONES DE LA APLICACIÓN
    # ========================================================================
    import config
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DEBUG'] = config.DEBUG
    
    return app
