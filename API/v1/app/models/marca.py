from bson import ObjectId
from app import mongo

class MarcaModel:
    @staticmethod
    def get_all():
        return list(mongo.db.marcas.find())

    @staticmethod
    def get_by_id(marca_id):
        return mongo.db.marcas.find_one({"_id": ObjectId(marca_id)})

    @staticmethod
    def create(data):
        return mongo.db.marcas.insert_one(data)

    @staticmethod
    def update(marca_id, data):
        return mongo.db.marcas.update_one({"_id": ObjectId(marca_id)}, {"$set": data})

    @staticmethod
    def delete(marca_id):
        return mongo.db.marcas.delete_one({"_id": ObjectId(marca_id)})