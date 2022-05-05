from django.contrib import admin
from .models import ToDoItem, ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['title']


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date']


admin.site.register(ToDoItem, ToDoItemAdmin)
admin.site.register(ToDoList, ToDoListAdmin)
