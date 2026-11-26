from flask import Blueprint, request, jsonify
from app.models.usuario import UsuarioModel
from app import token_required
from bson import ObjectId
from bson.errors import InvalidId

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=["GET"])
@token_required
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_all()
        for u in usuarios:
            u["_id"] = str(u["_id"])
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@usuarios_bp.route("/<id>", methods=["GET"])
@token_required
def get_usuario(id):
    try:
        u = UsuarioModel.get_by_id(id)
        if not u:
            return jsonify({"error": "Usuario no encontrado"}), 404
        u["_id"] = str(u["_id"])
        return jsonify(u), 200
    except InvalidId:
        return jsonify({"error": "ID inválido"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@usuarios_bp.route("/", methods=["POST"])
@token_required
def create_usuario():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Se requiere un JSON válido y el Header Content-Type: application/json"}), 400
    if "_id" in data and isinstance(data["_id"], str):
        try:
            data["_id"] = ObjectId(data["_id"])
        except InvalidId:
            pass
    result = UsuarioModel.create(data)
    return jsonify({"mensaje": "Usuario creado", "id": str(result.inserted_id)}), 201

@usuarios_bp.route("/<id>", methods=["PUT"])
@token_required
def update_usuario(id):
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Se requiere un JSON válido y el Header Content-Type: application/json"}), 400
    try:
        UsuarioModel.update(id, data)
        return jsonify({"mensaje": "Usuario actualizado"}), 200
    except InvalidId:
        return jsonify({"error": "ID inválido"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@usuarios_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_usuario(id):
    try:
        UsuarioModel.delete(id)
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    except InvalidId:
        return jsonify({"error": "ID inválido"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500