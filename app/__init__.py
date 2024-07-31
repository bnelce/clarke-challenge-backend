from flask import Flask
from .api.graphql.schema import schema
from ariadne import graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request
from .config.settings import Config
from .shared.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db) 
    
    type_defs = schema.type_defs
    resolvers = [schema.query, schema.mutation]
    executable_schema = make_executable_schema(type_defs, *resolvers)
    
    @app.route("/graphql", methods=["GET"])
    def graphql_playground():
        return PLAYGROUND_HTML, 200
    
    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()
        success, result = graphql_sync(
            executable_schema,
            data,
            context_value=request,
            debug=app.debug
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code
    
    return app
