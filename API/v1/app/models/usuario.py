from bson import ObjectId
from app import mongo

class UsuarioModel:
    @staticmethod
    def get_all():
        return list(mongo.db.usuarios.find())

    @staticmethod
    def get_by_id(user_id):
        return mongo.db.usuarios.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def create(data):
        return mongo.db.usuarios.insert_one(data)

    @staticmethod
    def update(user_id, data):
        return mongo.db.usuarios.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    @staticmethod
    def delete(user_id):
        return mongo.db.usuarios.delete_one({"_id": ObjectId(user_id)})