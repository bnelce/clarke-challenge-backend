from ariadne import QueryType
from app.models import Supplier

query = QueryType()


@query.field("suppliers")
def resolve_suppliers(_, info, consumption):
    return Supplier.query.filter(Supplier.min_kwh <= consumption).all()
