from django.contrib import admin
from hii.models import log

# Register your models here.

class logged(admin.ModelAdmin):
    list_display=('Username','Password')

admin.site.register(log,logged)