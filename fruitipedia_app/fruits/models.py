from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia_app.fruits.validators import only_letters_validator
from fruitipedia_app.profiles.models import Profile


# Create your models here.
class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2), only_letters_validator,
        ],
        error_messages={"unique": "This fruit name is already in use! Try a new one."}
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,

    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,)