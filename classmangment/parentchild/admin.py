from django.contrib import admin

# Register your models here.
from .models import parent,child,classes,enroll

@admin.register(parent)
class parentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']

@admin.register(child)
class childAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age' ,"parent_id"]


@admin.register(classes)
class classesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc' ,"seats"]

@admin.register(enroll)
class enrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'child_id', 'class_id']


