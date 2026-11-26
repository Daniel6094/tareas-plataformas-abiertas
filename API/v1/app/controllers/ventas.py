from flask import Blueprint, request, jsonify
from app.models.venta import VentaModel
from app import token_required
from bson import ObjectId
from datetime import datetime

ventas_bp = Blueprint("ventas", __name__)

@ventas_bp.route("/", methods=["GET"])
@token_required
def get_ventas():
    ventas = VentaModel.get_all()
    for v in ventas:
        v["_id"] = str(v["_id"])
        if "usuario_id" in v and v["usuario_id"]:
            v["usuario_id"] = str(v["usuario_id"])
        if "detalles" in v:
            for d in v["detalles"]:
                if "producto_id" in d and d["producto_id"]:
                    d["producto_id"] = str(d["producto_id"])
    return jsonify(ventas), 200

@ventas_bp.route("/<id>", methods=["GET"])
@token_required
def get_venta(id):
    v = VentaModel.get_by_id(id)
    if not v:
        return jsonify({"error": "Venta no encontrada"}), 404
    v["_id"] = str(v["_id"])
    if "usuario_id" in v and v["usuario_id"]:
        v["usuario_id"] = str(v["usuario_id"])
    if "detalles" in v:
        for d in v["detalles"]:
            if "producto_id" in d and d["producto_id"]:
                d["producto_id"] = str(d["producto_id"])
    return jsonify(v), 200

@ventas_bp.route("/", methods=["POST"])
@token_required
def create_venta():
    data = request.json
    if "_id" in data and isinstance(data["_id"], str):
        data["_id"] = ObjectId(data["_id"])
    if "usuario_id" in data and isinstance(data["usuario_id"], str):
        data["usuario_id"] = ObjectId(data["usuario_id"])
    if "fecha" in data and isinstance(data["fecha"], str):
        data["fecha"] = datetime.fromisoformat(data["fecha"].replace("Z", "+00:00"))
    if "detalles" in data:
        for d in data["detalles"]:
            if "producto_id" in d and isinstance(d["producto_id"], str):
                d["producto_id"] = ObjectId(d["producto_id"])
    result = VentaModel.create(data)
    return jsonify({"mensaje": "Venta creada", "id": str(result.inserted_id)}), 201

@ventas_bp.route("/<id>", methods=["PUT"])
@token_required
def update_venta(id):
    data = request.json
    VentaModel.update(id, data)
    return jsonify({"mensaje": "Venta actualizada"}), 200

@ventas_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_venta(id):
    VentaModel.delete(id)
    return jsonify({"mensaje": "Venta eliminada"}), 200