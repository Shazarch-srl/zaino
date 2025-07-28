from django.contrib import admin
from .models import Brand, Category, Item

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Brand)
