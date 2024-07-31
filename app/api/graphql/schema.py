from ariadne import QueryType, MutationType, make_executable_schema, gql
from .resolvers.supplier_resolver import resolve_suppliers
from .mutations.supplier_mutation import add_supplier

type_defs = gql("""
    type Query {
        suppliers(consumption: Int!): [Supplier!]
    }

    type Supplier {
        id: ID!
        name: String!
        logo: String!
        state: String!
        cost_per_kwh: Float!
        min_kwh: Int!
        total_clients: Int!
        average_rating: Float!
    }

    type Mutation {
        addSupplier(name: String!, logo: String!, state: String!, cost_per_kwh: Float!, min_kwh: Int!, total_clients: Int!, average_rating: Float!): Supplier!
    }
""")

query = QueryType()
mutation = MutationType()

query.set_field("suppliers", resolve_suppliers)
mutation.set_field("addSupplier", add_supplier)
