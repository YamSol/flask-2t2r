from pymongo import MongoClient
import json

class Client:
    def __init__(self, database, collection, host = 'mongodb://172.17.0.2', port=27017):
        self.client = MongoClient(host=host, port=port)
        if not self.client:
            raise Exception('Client couldn\'t connect to database')
        self.database = self.client.get_database(database)
        self.collection = self.database[collection]
    
    def __exit__(self):
        self.client.close()
    
    def get_all(self):
        result = self.collection.find()
        try:
            result_list = []
            for r in result:
                # update id key
                item = {}
                item['id'] = r.get('_id')
                item['checked'] = r.get('checked')
                item['name'] = r.get('name')
                result_list.append(item)
            return result_list
        except TypeError:
            return False
            # raise Exception('The table of elements cannot be converted to JSON format.')

    def __get_next_id(self):
        sequence = self.database['sequence_counters'].find_one_and_update(
            {"_id": "tasks"},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True
        )
        return sequence["seq"]

    def insert_one(self, name: str) -> bool:
        next_id = self.__get_next_id()
        response = self.collection.insert_one({"_id": next_id, "name":name, "checked":False})
        if response.inserted_id:
            return True
        return False

    def update_by_id(self, value_name: str, value: str, id: str):
        response = self.collection.find_one_and_update(
            {"_id": id},
            {"$set": {value_name:value}},
            return_document=False
        )
        if response:
            return True
        return False
    
    def delete_by_id(self, id: str):
        result = self.collection.delete_one({"_id":id})
        if result.deleted_count > 0:
            return True
        return False