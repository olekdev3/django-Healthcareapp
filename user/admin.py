from django.contrib import admin
from .models import Patient, Details, Profile

# Register your models here.
admin.site.register(Patient)
admin.site.register(Details)
admin.site.register(Profile)