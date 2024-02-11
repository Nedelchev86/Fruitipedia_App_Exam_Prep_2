from django.shortcuts import render
from django.views import generic as views

from fruitipedia_app.profiles.views import get_profile


# Create your views here.
class Homepage(views.TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = get_profile()
        return context