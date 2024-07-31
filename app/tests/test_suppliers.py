import pytest
from app import create_app, db
from app.domain.entities.suppiler import Supplier


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_add_supplier(client):
    mutation = """
    mutation {
        addSupplier(name: "Test Supplier", logo: "http://logo.url", state: "Test State", cost_per_kwh: 0.10, min_kwh: 500, total_clients: 100, average_rating: 4.5) {
            name
            logo
        }
    }
    """
    response = client.post("/graphql", json={'query': mutation})
    data = response.get_json()
    assert "errors" not in data
    assert data['data']['addSupplier']['name'] == "Test Supplier"


def test_suppliers(client):
    supplier = Supplier(name="Test Supplier", logo="http://logo.url", state="Test State", cost_per_kwh=0.10,
                        min_kwh=500, total_clients=100, average_rating=4.5)
    db.session.add(supplier)
    db.session.commit()

    query = """
    query {
        suppliers(consumption: 1000) {
            name
        }
    }
    """
    response = client.post("/graphql", json={'query': query})
    data = response.get_json()
    assert "errors" not in data
    assert data['data']['suppliers'][0]['name'] == "Test Supplier"
