from django.contrib import admin
from .models import Order
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# class OrderAdmin(UserAdmin):
#     list_display = ('product_names', 'total_products', 'total_amount',
#                     'created_at', 'updated_at')
#     search_fields = ('product_names', 'total_products')
#     readonly_fields = ('id', 'created_at', 'updated_at')
    
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

admin.site.register(Order)