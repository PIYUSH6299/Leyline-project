from flask import Flask, send_from_directory
from .config import Config
from .db import init_db
import os
from prometheus_flask_exporter import PrometheusMetrics
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the database
    init_db(app)
    
    # Initialize Prometheus metrics
    metrics = PrometheusMetrics(app)
    
    # Import and register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    # Swagger UI setup
    SWAGGER_URL = '/docs'  # URL for Swagger UI
    API_URL = '/swagger.json'  # URL for the swagger.json file

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI URL
        API_URL,      # Swagger JSON URL
        config={      # Swagger UI config overrides
            'app_name': "My REST API"
        }
    )

    # Register the blueprint for Swagger UI
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # Route to serve the swagger.json file
    @app.route('/swagger.json', methods=['GET'])
    def swagger_json():
        # Ensure Flask serves the static swagger.json file from the correct directory
        return send_from_directory(os.path.join(app.root_path, 'templates'), 'swagger.json')

    return app