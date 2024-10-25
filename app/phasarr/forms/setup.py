import sqlalchemy as sql

from flask_wtf import FlaskForm
from phasarr.models.user import User
from wtforms import PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo

from phasarr import db


class AuthenticationSetupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    auth_method = SelectField("Authentication Method", choices=[("form", "Login Form"), ("prompt", "Browser Prompt")])
    submit = SubmitField("Continue")

    def validate_username(self, username):
        user = db.session.scalar(sql.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")
        

class LibrariesSetupForm(FlaskForm):
    submit = SubmitField("Continue")

class DownloadSetupForm(FlaskForm):
    submit = SubmitField("Finish")