from django.contrib import admin

# Register your models here.
from .models import Product, Client


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'places', 'estoque')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)

