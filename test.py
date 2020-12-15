import pytest
from Class.TshirtProduct import TshirtProduct
from Class.SneakersProduct import SneakersProduct


def test_tshirt():
    print('test_tttt')
    tshirt = TshirtProduct(sku='0001', price=500.0, name="Kolobaza",
                               quantity=25, brand='Nike', tshirtsize=36, tshirtcolor='red')
    print(tshirt)
    assert tshirt.get_price() == 500 and tshirt.get_brand() == 'Nike'
