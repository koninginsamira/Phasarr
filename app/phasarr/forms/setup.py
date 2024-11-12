import os
from pathlib import Path
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

    def validate_username(self, field: Field):
        new_username = field.data
        is_different_username = new_username != self.previous_username.data

        if self.edit_user and is_different_username:
            user = db.session.scalar(sql.select(User).where(
                User.username == field.data))
            if user is not None:
                raise ValidationError("Please use a different username.")
        

class LibrariesSetupForm(Form):
    name = StringField("Name")
    path = HiddenField("Path", validators=[DataRequired()])
    submit = SubmitField("Add")

    def validate_path(self, field: Field):
        path = "." + field.data
        
        if os.path.isdir(path):
            return
        elif os.path.isfile(path):
            raise ValidationError("Please choose a folder, not a file.")
        else:
            raise ValidationError("Please choose an existing folder, and make sure it is accessible.")


class DownloadSetupForm(Form):
    submit = SubmitField("Finish")