import unittest
from unittest.mock import MagicMock, patch
from app import app
from services.employeeService import find_all
from services.productService import find_all
from services.orderService import find_all
from services.customerService import find_all
from services.productionService import find_all
from models.employee import Employee
from sqlalchemy.orm import Session
from database import db
from faker import Faker


class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


    @patch('services.employeeService.db.session.execute')
    def test_find_all(self, mock_execute):
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.name = "Tom"
        mock_employee.position = "CEO"

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_employee]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 1)
        self.assertEqual(response[0].name, "Tom")
        self.assertEqual(response[0].position, "CEO")


    @patch('services.employeeService.db.session.execute')
    def test_find_all2(self, mock_execute):
        mock_employee = MagicMock()
        mock_employee.id = 2
        mock_employee.name = "Jim"
        mock_employee.position = "CFO"

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_employee]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 2)
        self.assertEqual(response[0].name, "Jim")
        self.assertEqual(response[0].position, "CFO")
    
    


class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('services.productService.db.session.execute')
    def test_find_all(self, mock_execute):
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = 'shoes'
        mock_product.price = 19.99

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_product]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 1)
        self.assertEqual(response[0].name, "shoes")
        self.assertEqual(response[0].price, 19.99)


    @patch('services.productService.db.session.execute')
    def test_find_all2(self, mock_execute):
        mock_product = MagicMock()
        mock_product.id = 2
        mock_product.name = 'shirt'
        mock_product.price = 21.00

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_product]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 2)
        self.assertEqual(response[0].name, "shirt")
        self.assertEqual(response[0].price, 21.00)


class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('services.orderService.db.session.execute')
    def test_find_all(self, mock_execute):
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.product_id = 2
        mock_order.customer_id = 2
        mock_order.quantity = 2
        mock_order.total_price = 19.99

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_order]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 1)
        self.assertEqual(response[0].customer_id, 2)
        self.assertEqual(response[0].total_price, 19.99)


    @patch('services.orderService.db.session.execute')
    def test_find_all2(self, mock_execute):
        mock_order = MagicMock()
        mock_order.id = 2
        mock_order.product_id = 3
        mock_order.customer_id = 3
        mock_order.quantity = 3
        mock_order.total_price = 21.99

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_order]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 2)
        self.assertEqual(response[0].customer_id, 3)
        self.assertEqual(response[0].total_price, 21.99)

class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('services.customerService.db.session.execute')
    def test_find_all(self, mock_execute):
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = "John"
        mock_customer.email = "jdoe@gmail.com"
        mock_customer.phone = "8675309"

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_customer]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 1)
        self.assertEqual(response[0].name, "John")
        self.assertEqual(response[0].phone, "8675309")


    @patch('services.customerService.db.session.execute')
    def test_find_all2(self, mock_execute):
        mock_customer = MagicMock()
        mock_customer.id = 2
        mock_customer.name = "Jim"
        mock_customer.email = "jimdoe@gmail.com"
        mock_customer.phone = "5558675309"

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_customer]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 2)
        self.assertEqual(response[0].name, "Jim")
        self.assertEqual(response[0].phone, "5558675309")


class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('services.productionService.db.session.execute')
    def test_find_all(self, mock_execute):
        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = 2
        mock_production.quantity_produced = 15
        mock_production.date_produced = '2024-03-04'
        mock_production.employee_id = 2
        

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_production]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 1)
        self.assertEqual(response[0].quantity_produced, 15)
        self.assertEqual(response[0].employee_id, 2)


    @patch('services.productionService.db.session.execute')
    def test_find_all2(self, mock_execute):
        mock_production = MagicMock()
        mock_production.id = 2
        mock_production.product_id = 3
        mock_production.quantity_produced = 16
        mock_production.date_produced = '2034-03-09'
        mock_production.employee_id = 4
        

        mock_result = MagicMock()
        mock_result.scalars.return_value.all.return_value = [mock_production]

        mock_execute.return_value = mock_result

        response = find_all()

        self.assertEqual(response[0].id, 2)
        self.assertEqual(response[0].quantity_produced, 16)
        self.assertEqual(response[0].employee_id, 4)
        

if __name__ == "__main__":
    unittest.main()