from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from fruitipedia_app.fruits.forms import DeleteFruitForm
from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.profiles.views import get_profile


# Create your views here.
class Homepage(views.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_profile()
        return context


class Dashboard(views.ListView):
    model = Fruit
    template_name = "core/dashboard.html"


class AddFruit(views.CreateView):
    model = Fruit
    fields =["name", "image_url", "description", "nutrition"]
    template_name = "fruit/create-fruit.html"
    success_url = reverse_lazy("dashboard")


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].widget.attrs['placeholder'] = 'Fruit Name'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        form.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        form.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'

        for field in form.fields.values():
            field.label = ''
        return form

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)




class DetailsFruit(views.DetailView):
    model = Fruit
    template_name = "fruit/details-fruit.html"


class EditFruit(views.UpdateView):
    model = Fruit
    fields =["name", "image_url", "description", "nutrition"]
    template_name = "fruit/edit-fruit.html"
    success_url = reverse_lazy("dashboard")


class DeleteFruit(views.DeleteView):
    model = Fruit
    template_name = "fruit/delete-fruit.html"
    success_url = reverse_lazy("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteFruitForm(instance=self.object)
        return context
