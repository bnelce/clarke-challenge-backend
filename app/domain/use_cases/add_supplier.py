from app.repositories.supplier_repository import SupplierRepository

def add_supplier_use_case(name, logo, state, cost_per_kwh, min_kwh, total_clients, average_rating):
    supplier = SupplierRepository.create_supplier(name, logo, state, cost_per_kwh, min_kwh, total_clients, average_rating)
    return supplier
