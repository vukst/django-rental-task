from django.contrib import admin

# Register your models here.
from .models import Rental, Reservation

admin.site.register(Rental)
admin.site.register(Reservation)
