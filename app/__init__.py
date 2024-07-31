# __init__.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne import make_executable_schema, graphql_sync, snake_case_fallback_resolvers
from ariadne.explorer.playground import PLAYGROUND_HTML
from ariadne.asgi import GraphQL

from app.api.graphql.schema import mutation, query, type_defs

from shared.database import db, migrate
from config.settings import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    schema = make_executable_schema(type_defs, query, mutation, snake_case_fallback_resolvers)
    graphql_app = GraphQL(schema, debug=True)

    @app.route("/graphql", methods=["GET"])
    def graphql_playground():
        return PLAYGROUND_HTML, 200

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()
        success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
        return jsonify(result), 200 if success else 400

    return app
