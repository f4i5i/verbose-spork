from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import TemplateView




class HomeView(TemplateView):
    template_name = 'home.html'




