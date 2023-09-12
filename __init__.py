from flask import Flask
from flask_mail import Mail, Message
from flask_admin import Admin
import flask_sqlalchemy
import os

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.update(dict(
  PREFERRED_URL_SCHEME = 'https'
))

# Restrict the maximum file upload to 16mb
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db = db)
admin = Admin(app, name='karlduckett.com', template_mode='bootstrap3')

# Create the dash apps
from app.dash_application import create_dash_application, whittakers_dash_dashboard, gapminder_dash_application

# Import routing to render the pages
from app import views, models
