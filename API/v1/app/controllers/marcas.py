from flask import Blueprint, request, jsonify
from app.models.marca import MarcaModel
from app import mongo, token_required
from bson import ObjectId

marcas_bp = Blueprint("marcas", __name__)

@marcas_bp.route("/", methods=["GET"])
@token_required
def get_marcas():
    marcas = MarcaModel.get_all()
    for m in marcas:
        m["_id"] = str(m["_id"])
    return jsonify(marcas), 200

@marcas_bp.route("/<id>", methods=["GET"])
@token_required
def get_marca(id):
    m = MarcaModel.get_by_id(id)
    if not m:
        return jsonify({"error": "Marca no encontrada"}), 404
    m["_id"] = str(m["_id"])
    return jsonify(m), 200

@marcas_bp.route("/", methods=["POST"])
@token_required
def create_marca():
    data = request.json
    if "_id" in data and isinstance(data["_id"], str):
        data["_id"] = ObjectId(data["_id"])
    result = MarcaModel.create(data)
    return jsonify({"mensaje": "Marca creada", "id": str(result.inserted_id)}), 201

@marcas_bp.route("/<id>", methods=["PUT"])
@token_required
def update_marca(id):
    data = request.json
    MarcaModel.update(id, data)
    return jsonify({"mensaje": "Marca actualizada"}), 200

@marcas_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_marca(id):
    MarcaModel.delete(id)
    return jsonify({"mensaje": "Marca eliminada"}), 200

@marcas_bp.route("/reportes/marcas-con-ventas", methods=["GET"])
@token_required
def reporte_marcas_con_ventas():
    pipeline = [
        {"$unwind": "$detalles"},
        {"$group": {"_id": "$detalles.marca_nombre"}},
        {"$project": {"_id": 0, "marca": "$_id"}}
    ]
    resultado = list(mongo.db.ventas.aggregate(pipeline))
    return jsonify(resultado), 200

@marcas_bp.route("/reportes/top-5-marcas", methods=["GET"])
@token_required
def reporte_top_marcas():
    pipeline = [
        {"$unwind": "$detalles"},
        {"$group": {"_id": "$detalles.marca_nombre", "total_unidades_vendidas": {"$sum": "$detalles.cantidad"}}},
        {"$sort": {"total_unidades_vendidas": -1}},
        {"$limit": 5}
    ]
    resultado = list(mongo.db.ventas.aggregate(pipeline))
    for r in resultado:
        r["marca"] = r.pop("_id")
    return jsonify(resultado), 200