from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','father_name','email','phone_num','gender','dob','course','address','photo','aadhar','booking_date','booked_on','fee']
admin.site.register(Student,StudentAdmin)
class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
admin.site.register(product,prodadmin)
