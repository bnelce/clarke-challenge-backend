from ariadne import MutationType
from  app.domain.entities.suppiler import db, Supplier

mutation = MutationType()


@mutation.field("addSupplier")
def resolve_add_supplier(_, info, input):
    new_supplier = Supplier(**input)
    db.session.add(new_supplier)
    db.session.commit()
    return new_supplier
