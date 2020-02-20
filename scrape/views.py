from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView
import  django_rq

from .tasks import scrape
from .models import Ittf

class HomeView(TemplateView):
    template_name = 'home.html'



def scrapeview(request):
    if request.method == "GET":
        queue= django_rq.get_queue('default',is_async=True,default_timeout=30000)
        queue.enqueue(scrape)



class IttfView(ListView):
    model = Ittf
    template_name = "Table.html"
    
