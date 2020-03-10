from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Competition)
admin.site.register(RawData)
admin.site.register(Phases)
admin.site.register(Table)