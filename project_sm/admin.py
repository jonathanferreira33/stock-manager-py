from django.contrib import admin
from project_sm.models import Product

class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Product, Products)

