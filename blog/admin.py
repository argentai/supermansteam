from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hospital)
admin.site.register(GlavVrach)
admin.site.register(Lech_vrach)
admin.site.register(Medsestra)
admin.site.register(Pacient)