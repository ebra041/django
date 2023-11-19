from django.contrib import admin
from .models import Food, Bill, BillOrders

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display=("id","foodname","quantity", "description","cost","image",)
admin.site.register(Food,FoodAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display=("id","employee","client", "bdate",)
admin.site.register(Bill,BillAdmin)

class BillOrdersAdmin(admin.ModelAdmin):
    list_display=("id","order", "bill",)
admin.site.register(BillOrders,BillOrdersAdmin)