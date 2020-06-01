# core/admin.py

from django.contrib import admin
from .models import Movie  # add this
# Register your models here.

admin.site.register(Movie) # add this