
from django.db import models as forms
from django.forms import ModelForm

from fruitipedia_app.fruits.models import Fruit


class DeleteFruitForm(ModelForm):
    class Meta:
        model = Fruit
        fields = ["name", "image_url", "description", "nutrition"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
