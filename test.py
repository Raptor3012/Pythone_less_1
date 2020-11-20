import pymongo
from bson.objectid import ObjectId


mongo_client = pymongo.MongoClient("localhost")

def create_collection(db_name: str, collection:str):
    db = mongo_client[db_name]
    collection = db[collection]

def add_product(name: str, count: int, manufacturer: str, price: int, size: int) -> str:
    id = mongo_client.product.sneakers.insert_one({'Name': name, 'Count': count, 'Manufacturer': manufacturer, 'Price': price, 'Size': size})
    return id.inserted_id

def update_product(product_id, field, new_value):
    mongo_client.product.sneakers.update_one({'_id': ObjectId(product_id)}, {'$set': {field: new_value}})

def delete_product(product_id):
    mongo_client.product.sneakers.delete_one({'_id': ObjectId(product_id)})