from ariadne import gql

type_defs = gql("""
    type Query {
        suppliers(consumption: Int!): [Supplier!]!
    }

    type Mutation {
        addSupplier(input: AddSupplierInput!): Supplier
    }

    input AddSupplierInput {
        name: String!
        logo: String!
        state: String!
        cost_per_kwh: Float!
        min_kwh: Int!
        total_clients: Int!
        avg_rating: Float!
    }
    
    type Supplier {
        id: ID!
        name: String!
        logo: String!
        state: String!
        cost_per_kwh: Float!
        min_kwh: Int!
        total_clients: Int!
        avg_rating: Float!
    }
""")
