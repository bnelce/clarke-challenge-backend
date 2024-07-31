from app.domain.use_cases.get_suppliers import get_suppliers

def resolve_suppliers(_, info, consumption):
    return get_suppliers(consumption)
