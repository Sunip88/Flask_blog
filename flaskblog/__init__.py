import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '0956216755cc68d17ee4ee8862451d93'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginmenager = LoginManager(app)
loginmenager.login_view = 'login'
loginmenager.login_message_category = 'info'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('EMAIL_USER'),  # I checked on fixed mail and pass and it works
    "MAIL_PASSWORD": os.environ.get('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

from flaskblog import routes