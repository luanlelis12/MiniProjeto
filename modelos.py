from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite::///test.db'

class 