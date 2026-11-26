from bson import ObjectId
from app import mongo

class ProductoModel:
    @staticmethod
    def get_all():
        return list(mongo.db.productos.find())

    @staticmethod
    def get_by_id(producto_id):
        return mongo.db.productos.find_one({"_id": ObjectId(producto_id)})

    @staticmethod
    def create(data):
        return mongo.db.productos.insert_one(data)

    @staticmethod
    def update(producto_id, data):
        return mongo.db.productos.update_one({"_id": ObjectId(producto_id)}, {"$set": data})

    @staticmethod
    def delete(producto_id):
        return mongo.db.productos.delete_one({"_id": ObjectId(producto_id)})