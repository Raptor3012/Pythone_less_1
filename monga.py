import pymongo
import os
from bson.objectid import ObjectId


mongo_client = pymongo.MongoClient(host="localhost:27017")

def Create_collection(db_name: str='product', collection:str='sneakers'):
    db = mongo_client[db_name]
    collection = db[collection]

def Add_product(name: str, count: int, manufacturer: str, price: int, size: int) -> str:
    id = mongo_client.product.sneakers.insert_one({'Name': name, 'Count': count, 'Manufacturer': manufacturer, 'Price': price, 'Size': size})
    return id.inserted_id

def Update_product(product_id, field, new_value):
    mongo_client.product.sneakers.update_one({'_id': ObjectId(product_id)}, {'$set': {field: new_value}})

def Delete_product(product_id):
    mongo_client.product.sneakers.delete_one({'_id': ObjectId(product_id)})
    
def Print_data():
    result = mongo_client.product.sneakers.find()
    return result

def LoadDataFromFile(filepath):        
    if os.path.exists(filepath):
        f = open(filepath, 'r')
        for line in f:
            inp = line.split(' ')
            inp = [line.rstrip('\n') for line in inp]
            Add_product(inp[0],inp[1],inp[2],inp[3],inp[4])
        f.close()

