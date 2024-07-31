from app.domain.entities.suppiler import Supplier
from shared.database import db

class SupplierRepository:
    @staticmethod
    def get_suppliers_by_consumption(consumption):
        return Supplier.query.filter(Supplier.min_kwh <= consumption).all()

    @staticmethod
    def create_supplier(name, logo, state, cost_per_kwh, min_kwh, total_clients, average_rating):
        supplier = Supplier(
            name=name,
            logo=logo,
            state=state,
            cost_per_kwh=cost_per_kwh,
            min_kwh=min_kwh,
            total_clients=total_clients,
            average_rating=average_rating
        )
        db.session.add(supplier)
        db.session.commit()
        return supplier
