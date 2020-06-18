from django.contrib import admin
from shoestore_app.models import FootWear, Shoe

admin.site,register(FootWear)
admin.site.register(Shoe)

