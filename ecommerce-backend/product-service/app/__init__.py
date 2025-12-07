from flask import Flask
from .db import db
from .routes.product_routes import product_bp
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)

    # PostgreSQL configuration
    # Use DATABASE_URL environment variable if set,
    # otherwise fallback to the correct Kubernetes service URL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:a@postgres.database.svc.cluster.local:5432/products_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB and Migrations
    db.init_app(app)
    Migrate(app, db)

    # Register API routes
    app.register_blueprint(product_bp)

    return app
