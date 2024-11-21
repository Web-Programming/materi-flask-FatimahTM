from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create Flask app instance
app = Flask(__name__)

# Configure the app to connect to the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/myflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary track modifications

# Initialize the database and migration manager
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes (make sure routes.py exists in your project)
from routes import *

# Run the app only if this script is run directly (not imported)
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development purposes
