from django.contrib import admin
from .models import abc, post
# Register your models here.

#for displaying emid and empname without open abc
class abcAdmin(admin.ModelAdmin):
    list_display=['empid','empname']
admin.site.register(abc,abcAdmin)


admin.site.register(post)