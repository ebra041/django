from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id","fname","sname","password","slug",)
admin.site.register(User,UserAdmin)