from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,AnyOf

class User(FlaskForm):
    username = StringField('Username',validators=[InputRequired('username is required!'),Length(min=2,max=15,message="username must be between 2 and 15 characters")])
    email = StringField('Email',validators=[InputRequired('email is required!')])
    password = PasswordField("Password",validators=[InputRequired('password is required!')])
    confirmpassword = PasswordField("ConfirmPassword",validators=[InputRequired('password is required!')])
    submit = SubmitField("Signup")