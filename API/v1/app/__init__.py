import os
from functools import wraps

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

mongo = PyMongo()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"error": "Token mal formado"}), 401
        
        if not token or token != "mi_token_secreto_123":
            return jsonify({"error": "Token inválido o ausente"}), 401
        return f(*args, **kwargs)
    return decorated

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://danielvegav6094_db_user:1234@cluster0.byjrbup.mongodb.net/pc_gaming_db?retryWrites=true&w=majority"
    
    mongo.init_app(app)

    allowed_origins = {
        origin.strip()
        for origin in os.environ.get(
            "FRONTEND_ORIGINS",
            "http://127.0.0.1:5500,http://localhost:5500",
        ).split(",")
        if origin.strip()
    }

    @app.after_request
    def add_cors_headers(response):
        origin = request.headers.get("Origin")
        if origin in allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response.vary.add("Origin")
        return response

    from app.index import index_bp
    from app.controllers.usuarios import usuarios_bp
    from app.controllers.marcas import marcas_bp
    from app.controllers.productos import productos_bp
    from app.controllers.ventas import ventas_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(usuarios_bp, url_prefix="/api/v1/usuarios")
    app.register_blueprint(marcas_bp, url_prefix="/api/v1/marcas")
    app.register_blueprint(productos_bp, url_prefix="/api/v1/productos")
    app.register_blueprint(ventas_bp, url_prefix="/api/v1/ventas")

    return app