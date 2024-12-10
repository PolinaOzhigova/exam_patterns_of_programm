from warehouse_model import WarehouseModel
from organization_model import OrganizationModel
from user_model import UserModel
import unittest

class TestFactoryMethod(unittest.TestCase):
    def test_user_model_factory(self):
        """Тест фабричного метода UserModel.create"""
        name = " John Doe "
        user = UserModel.create(name)
        self.assertEqual(user.name, "John Doe")

    def test_organization_model_factory(self):
        """Тест фабричного метода OrganizationModel.create"""
        name = " 1C "
        org = OrganizationModel.create(name)
        self.assertEqual(org.name, "1C")

    def test_warehouse_factory(self):
        """Тест фабричного метода Warehouse.create"""
        address = " 123 Main Street "
        warehouse = WarehouseModel.create(address)
        self.assertEqual(warehouse.address, "123 Main Street")

if __name__ == "__main__":
    unittest.main()