from django.contrib import admin
from .models import Tasks
# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'starred', 'completed')  # Fields to display in the list view
    search_fields = ('title', 'description')  # Fields to search
    list_filter = ('priority', 'starred', 'completed', 'overdue')  # Fields to filter by

# Register the model with the admin site
admin.site.register(Tasks, TasksAdmin)