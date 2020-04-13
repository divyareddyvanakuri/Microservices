from app import app
from flask import render_template,jsonify,session,url_for,redirect,request
from flask_mail import Mail,Message
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import URLSafeTimedSerializer,SignatureExpired
import jwt
import uuid
import os
from flask_wtf.csrf import CSRFProtect,CSRFError
from .form import User

url_serializer = URLSafeTimedSerializer('Thisissecret!')

app.config.update(dict(
    SECRET_KEY=os.environ['SECRET_KEY'],
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

app.config.update(
	MAIL_DEBUG =True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
    MAIL_USE_TLS = False,
	MAIL_USERNAME = os.environ['EMAIL_USER'],
	MAIL_PASSWORD = os.environ['EMAIL_PASSWORD'],
    MAIL_DEFAULT_SENDER = os.environ['EMAIL_USER']
	)

mail = Mail(app)
csrf = CSRFProtect(app)

@app.route('/')
def home():
   return render_template("home.html")
