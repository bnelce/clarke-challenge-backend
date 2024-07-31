from app.repositories.supplier_repository import SupplierRepository

def get_suppliers(consumption):
    return SupplierRepository.get_suppliers_by_consumption(consumption)
