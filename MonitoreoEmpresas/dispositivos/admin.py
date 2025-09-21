from django.contrib import admin
from .models import Category, Zone, Device, Measurement, Alert

# Hemos quitado Organization de aquí porque ya está registrado en su propia app
admin.site.register(Category)
admin.site.register(Zone)
admin.site.register(Device)
admin.site.register(Measurement)
admin.site.register(Alert)