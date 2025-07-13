from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy object to manage database operations
db = SQLAlchemy()

def create_app():
    # Create the Flask application and specify the folder for HTML templates
    app = Flask(__name__, template_folder='templates')

    # Configure the SQLite database path
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    
    # Bind the SQLAlchemy instance to the app
    db.init_app(app)
    
    # Import and register the application routes
    from routes import register_routes
    register_routes(app, db)
    
    # Set up database migration support
    migrate = Migrate(app, db)
    
    # Return the fully configured Flask app
    return app
