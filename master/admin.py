from django.contrib import admin
from master.models import Country, Menu, Region, City

# Register your models here.
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Menu)
