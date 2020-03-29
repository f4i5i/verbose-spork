from django import forms
from url_filter.filtersets import ModelFilterSet
from .models import *

class PlayerFilter(ModelFilterSet):
    class Meta:
        model = Player
        