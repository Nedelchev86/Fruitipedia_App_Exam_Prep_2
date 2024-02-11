from django.forms import PasswordInput
from django.shortcuts import render
from django.urls import reverse_lazy

from fruitipedia_app.fruits.models import Fruit
from fruitipedia_app.profiles.models import Profile
from django.views import generic as views

# Create your views here.
def get_profile():
    try:
        profile = Profile.objects.get()
    except:
        return None
    return profile


class CreateProfile(views.CreateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email', 'password']
    template_name = "profile/create-profile.html"
    success_url = reverse_lazy("homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_profile()
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        form.fields['email'].widget.attrs['placeholder'] = 'Email'
        form.fields['password'].widget.attrs['placeholder'] = 'Password'

        form.fields['password'].widget = PasswordInput()

        for field in form.fields.values():
            field.label = ''
        return form


class DetailsProfile(views.DetailView):
    model = Profile
    template_name = "profile/details-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Fruit.objects.all().count()
        return context

    def get_object(self, queryset=None):
        return get_profile()


class EditProfile(views.UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "image_url", "age"]
    template_name = "profile/edit-profile.html"
    success_url = reverse_lazy("details profile")

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfile(views.DeleteView):
    model = Profile
    template_name = "profile/delete-profile.html"
    success_url = reverse_lazy("homepage")

    def get_object(self, queryset=None):
        return get_profile()




