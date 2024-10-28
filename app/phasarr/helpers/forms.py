from wtforms.validators import DataRequired


def is_required(field):
    return any(isinstance(validator, DataRequired) for validator in field.validators)