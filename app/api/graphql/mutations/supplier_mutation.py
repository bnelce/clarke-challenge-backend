from app.domain.use_cases.add_supplier import add_supplier_use_case

def add_supplier(_, info, name, logo, state, cost_per_kwh, min_kwh, total_clients, average_rating):
    return add_supplier_use_case(name, logo, state, cost_per_kwh, min_kwh, total_clients, average_rating)
