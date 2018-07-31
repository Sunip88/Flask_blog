from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '0956216755cc68d17ee4ee8862451d93'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmenager = LoginManager(app)
loginmenager.login_view = 'login'
loginmenager.login_message_category = 'info'

from flaskblog import routes