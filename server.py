from usuarios_app import app #Python sabe que debe empezar a buscar en __init__
from usuarios_app.controladores import controlador_usuarios
# ...server.py

if __name__ == "__main__":
    app.run(debug=True)