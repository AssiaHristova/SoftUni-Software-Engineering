from django.core.exceptions import ValidationError


def validate_max_value(max_value):
    def validate(value):
        if value > max_value:
            raise ValidationError(f'Value can not be greater than {max_value}')
    return validate
