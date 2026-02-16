"""
ARCHIVO PRINCIPAL DE LA APLICACIÓN - run.py
Este archivo inicia la aplicación Flask.

PASO 5: Ejecutar la aplicación
"""

from app import create_app

# ============================================================================
# CREAR Y EJECUTAR LA APLICACIÓN
# ============================================================================

if __name__ == '__main__':
    # Crear la aplicación usando la factory function
    app = create_app()
    
    # ========================================================================
    # EXPLICACIÓN DE LA EJECUCIÓN:
    # ========================================================================
    # 1. host='0.0.0.0'   → Accesible desde cualquier dirección IP
    # 2. port=5000        → Puerto donde corre la aplicación
    # 3. debug=True       → Modo depuración (recarga automática en cambios)
    # 4. use_reloader=True → Reinicia el servidor cuando cambias archivos
    #
    # CÓMO ACCEDER:
    # - Abre el navegador en: http://localhost:5000
    # - O desde otra máquina: http://<tu_ip>:5000
    # ========================================================================
    
    print("=" * 70)
    print("🚀 INICIANDO APLICACIÓN FLASK - CRUD CLIENTES")
    print("=" * 70)
    print("✓ Servidor corriendo en: http://localhost:5000")
    print("✓ Modo DEBUG: Activado (reinicio automático de cambios)")
    print("✓ Presiona CTRL+C para detener el servidor")
    print("=" * 70)
    print()
    
    # Ejecutar la aplicación
    app.run(
        host='0.0.0.0',      # Escuchar en todas las interfaces
        port=5000,           # Puerto 5000
        debug=True,          # Modo depuración
        use_reloader=True    # Reiniciar al cambiar archivos
    )
