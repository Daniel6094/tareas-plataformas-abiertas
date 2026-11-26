from flask import Blueprint, request, jsonify
from app.models.producto import ProductoModel
from app import mongo, token_required
from bson import ObjectId

productos_bp = Blueprint("productos", __name__)

def serialize_object_ids(value):
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, list):
        return [serialize_object_ids(item) for item in value]
    if isinstance(value, dict):
        return {key: serialize_object_ids(item) for key, item in value.items()}
    return value

@productos_bp.route("/", methods=["GET"])
@token_required
def get_productos():
    productos = ProductoModel.get_all()
    return jsonify(serialize_object_ids(productos)), 200

@productos_bp.route("/<id>", methods=["GET"])
@token_required
def get_producto(id):
    p = ProductoModel.get_by_id(id)
    if not p:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(serialize_object_ids(p)), 200

@productos_bp.route("/", methods=["POST"])
@token_required
def create_producto():
    data = request.json
    if "_id" in data and isinstance(data["_id"], str):
        data["_id"] = ObjectId(data["_id"])
    if "marca_id" in data and isinstance(data["marca_id"], str):
        data["marca_id"] = ObjectId(data["marca_id"])
    result = ProductoModel.create(data)
    return jsonify({"mensaje": "Producto creado", "id": str(result.inserted_id)}), 201

@productos_bp.route("/<id>", methods=["PUT"])
@token_required
def update_producto(id):
    data = request.json
    if "marca_id" in data and isinstance(data["marca_id"], str):
        data["marca_id"] = ObjectId(data["marca_id"])
    ProductoModel.update(id, data)
    return jsonify({"mensaje": "Producto actualizado"}), 200

@productos_bp.route("/<id>", methods=["DELETE"])
@token_required
def delete_producto(id):
    ProductoModel.delete(id)
    return jsonify({"mensaje": "Producto eliminado"}), 200

@productos_bp.route("/reportes/stock-restante", methods=["GET"])
@token_required
def reporte_stock_restante():
    pipeline = [
        {"$unwind": "$detalles"},
        {
            "$group": {
                "_id": "$detalles.producto_id",
                "nombre_producto": {"$first": "$detalles.producto_nombre"},
                "cantidad_vendida": {"$sum": "$detalles.cantidad"}
            }
        },
        {
            "$lookup": {
                "from": "productos",
                "localField": "_id",
                "foreignField": "_id",
                "as": "info_producto"
            }
        },
        {"$unwind": "$info_producto"},
        {
            "$project": {
                "_id": {"$toString": "$_id"},
                "nombre_producto": 1,
                "cantidad_vendida": 1,
                "stock_restante": "$info_producto.stock"
            }
        }
    ]
    resultado = list(mongo.db.ventas.aggregate(pipeline))
    return jsonify(resultado), 200