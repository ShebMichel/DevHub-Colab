from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # Register blueprints
    from app.routes import business, customer, appointment, inventory, notification
    app.register_blueprint(business.bp)
    app.register_blueprint(customer.bp)
    app.register_blueprint(appointment.bp)
    app.register_blueprint(inventory.bp)
    app.register_blueprint(notification.bp)
    
    # Home route
    @app.route('/')
    def index():
        return '''
        <h1>🚀 Perth SMB Automation API</h1>
        <p>Flask-based automation system for Perth small businesses</p>
        <h2>API Endpoints</h2>
        <ul>
            <li>GET /api/businesses - List all businesses</li>
            <li>POST /api/businesses - Create new business</li>
            <li>GET /api/businesses/&lt;id&gt;/customers - Get customers</li>
            <li>POST /api/customers - Create customer</li>
            <li>GET /api/businesses/&lt;id&gt;/appointments - Get appointments</li>
            <li>POST /api/appointments - Create appointment</li>
            <li>GET /api/businesses/&lt;id&gt;/inventory - Get inventory</li>
            <li>POST /api/inventory - Create inventory item</li>
        </ul>
        '''
    
    return app