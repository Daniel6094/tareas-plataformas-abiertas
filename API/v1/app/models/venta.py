from bson import ObjectId
from app import mongo

class VentaModel:
    @staticmethod
    def get_all():
        return list(mongo.db.ventas.find())

    @staticmethod
    def get_by_id(venta_id):
        return mongo.db.ventas.find_one({"_id": ObjectId(venta_id)})

    @staticmethod
    def create(data):
        return mongo.db.ventas.insert_one(data)

    @staticmethod
    def update(venta_id, data):
        return mongo.db.ventas.update_one({"_id": ObjectId(venta_id)}, {"$set": data})

    @staticmethod
    def delete(venta_id):
        return mongo.db.ventas.delete_one({"_id": ObjectId(venta_id)})