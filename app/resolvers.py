from ariadne import ObjectType

from app.mutations.add_supplier import resolve_add_supplier
from app.queries.suppliers import resolve_suppliers

mutation = ObjectType("Mutation")
mutation.set_field("addSupplier", resolve_add_supplier)

query = ObjectType("Query")
query.set_field("suppliers", resolve_suppliers)
