import pytest
import pymongo
from Class.TshirtProduct import TshirtProduct
from Class.SneakersProduct import SneakersProduct

mongo_client = pymongo.MongoClient(host="localhost:27017")

tshirt = TshirtProduct(sku='0001', price=500, name="Dad",
                       quantity=25, brand='Nike', tshirtsize='M', tshirtcolor='red')
sneakers = SneakersProduct(sku='0002', price=500, name="Dad",
                           quantity=25, brand='Nike', sneakerssize=36, sneakerscolor='red')


def test_tshirt():
    assert tshirt.get_price() == 500 and tshirt.get_tshirtcolor()== 'red'


def test_sneakers():
    assert sneakers.get_price() == 500 and sneakers.get_sneakerssize() == 36


def test_database_find():
    tshirt.Add_product(mongo_client)
    result_find = TshirtProduct.find_product(mongo_client, "0001")
    print(result_find)
    assert result_find["Price"] == tshirt.get_price()


def test_database_delete():
    tshirt.Add_product(mongo_client)
    TshirtProduct.Delete_product(mongo_client, '0001')
    result_find = TshirtProduct.find_product(mongo_client, '0001')
    assert result_find
