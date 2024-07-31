import unittest
from app import create_app
from app.shared.database import db
from app.domain.entities.supplier import Supplier

class TestGetSuppliers(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()
        self.populate_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def populate_db(self):
        supplier1 = Supplier(
            name="Supplier1",
            logo="logo1.png",
            state="SP",
            cost_per_kwh=0.50,
            min_kwh=10000,
            total_clients=500,
            average_rating=4.5
        )
        supplier2 = Supplier(
            name="Supplier2",
            logo="logo2.png",
            state="RJ",
            cost_per_kwh=0.45,
            min_kwh=15000,
            total_clients=1000,
            average_rating=4.7
        )
        db.session.add(supplier1)
        db.session.add(supplier2)
        db.session.commit()

    def test_get_suppliers_above_min_kwh(self):
        query = """
        query {
            suppliers(consumption: 20000) {
                name
                cost_per_kwh
            }
        }
        """
        result = self.client.post('/graphql', json={'query': query})
        self.assertEqual(result.status_code, 200)
        data = result.get_json()
        self.assertEqual(len(data['data']['suppliers']), 2)

    def test_get_suppliers_below_min_kwh(self):
        query = """
        query {
            suppliers(consumption: 5000) {
                name
                cost_per_kwh
            }
        }
        """
        result = self.client.post('/graphql', json={'query': query})
        self.assertEqual(result.status_code, 200)
        data = result.get_json()
        self.assertEqual(len(data['data']['suppliers']), 0)
