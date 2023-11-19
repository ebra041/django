from django.contrib import admin
from .models import Student,Course,Course_Join
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=("id","fname","sname","join_date",)
admin.site.register(Student,StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=("id","cname","cduration",)
admin.site.register(Course,CourseAdmin)

class Course_JoinAdmin(admin.ModelAdmin):
    list_display=("sid","cid",)
admin.site.register(Course_Join,Course_JoinAdmin)