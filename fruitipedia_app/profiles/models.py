from django.core.validators import MinLengthValidator
from django.db import models
from django import forms

from fruitipedia_app.profiles.validators import first_letter_validator


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2),
                    first_letter_validator],
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1),
                    first_letter_validator],
    )

    email = models.EmailField(
        max_length=40,
        unique=True,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text= "*Password length requirements: 8 to 20 characters",
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default= 18,
        null=True,
        blank=True,
    )