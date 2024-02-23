from django.contrib import admin
from .models import Invoice,Invoice_detail
# Register your models here.
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'customer_name']

@admin.register(Invoice_detail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'quantity', 'unit_price', 'price']