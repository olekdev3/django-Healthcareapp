from django.contrib import admin
from .models import Patient, Details

# Register your models here.
admin.site.register(Patient)
admin.site.register(Details)