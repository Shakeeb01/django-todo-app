from django.contrib import admin
from .models import Task

# Registering Model on admin site.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','description','task_status','created_at']
    
