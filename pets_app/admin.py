from django.contrib import admin

from pets_app.models.pet import Pet, Owner


admin.site.register(Pet)
admin.site.register(Owner)