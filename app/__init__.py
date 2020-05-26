from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
#csrf = CsrfProtect(app)

# These must be last to avoid recursion
from app import routes, models