from phasarr.classes.form import Form
import sqlalchemy as sql

from phasarr.models.user import User
from wtforms import Field, HiddenField, PasswordField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Optional

from phasarr import db


class AuthSetupForm(Form):
    edit_user: bool = False
    edit_auth_mode: bool = False

    previous_username = HiddenField()
    username = StringField("Username")
    password = PasswordField("Password")
    password2 = PasswordField("Repeat Password")
    auth_method = SelectField(
        "Authentication Method", 
        choices=[("form", "Login Form"), ("prompt", "Browser Prompt")])
    submit = SubmitField("Save and continue")

    def __init__(self, edit_user: bool = False, edit_auth_mode: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        required_unless_edit_user = DataRequired() if not edit_user else Optional()
        required_unless_edit_auth_mode = DataRequired() if not edit_auth_mode else Optional()

        self.edit_user = edit_user
        self.edit_auth_mode = edit_auth_mode

        self.username.validators = [required_unless_edit_user]
        self.password.validators = [required_unless_edit_user]
        self.password2.validators = [EqualTo("password"), required_unless_edit_user]
        self.auth_method.validators = [required_unless_edit_auth_mode]

    def validate_username(self, username: Field):
        if self.edit_user and username.data != self.previous_username.data:
            user = db.session.scalar(sql.select(User).where(
                User.username == username.data))
            if user is not None:
                raise ValidationError("Please use a different username.")
        

class LibrariesSetupForm(Form):
    submit = SubmitField("Save and continue")

class DownloadSetupForm(Form):
    submit = SubmitField("Finish")