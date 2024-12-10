from flask import Flask
from flask_cors import CORS
from .routes import init_app

def create_app():
    app = Flask(__name__)

    # Configuración de CORS
    CORS(app)

    # Registrar las rutas desde routes.py
    init_app(app)

    return app
