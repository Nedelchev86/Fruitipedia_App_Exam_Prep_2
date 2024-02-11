from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpsha():
            raise ValidationError("Fruit name should contain only letters!")