from flask import Blueprint, jsonify

index_bp = Blueprint("index", __name__)

@index_bp.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API PC Gaming Store activa", "version": "v1"})