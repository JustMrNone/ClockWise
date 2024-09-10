from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'date', 'repeat', 'priority', 'status', 'due_date')

    # Add filters to the list view
    list_filter = ('status', 'priority', 'repeat', 'date')

    # Search functionality
    search_fields = ('title', 'description')

    # Fields to be editable in the list view
    list_editable = ('status', 'priority')

    # Group fields for the form view
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'steps', 'status')
        }),
        ('Scheduling', {
            'fields': ('date', 'due_date', 'repeat')
        }),
        ('Priority', {
            'fields': ('priority',)
        }),
    )

    # Add a date hierarchy filter
    date_hierarchy = 'date'

# Register the model and admin customization
admin.site.register(Task, TaskAdmin)