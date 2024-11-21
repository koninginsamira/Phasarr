from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class Form(FlaskForm):
    def is_field_required(self, field_name):
        field = getattr(self, field_name)
        return any(isinstance(validator, DataRequired) for validator in field.validators)

    def clear(self):
        for field in self:
            field.data = None