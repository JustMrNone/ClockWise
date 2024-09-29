from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import Tasks
from django.utils import timezone
import json
from django.http import HttpResponseNotFound


# Create your views here.

class Today(View):
    def get(self, request):
        tasks = Tasks.objects.filter(due_date__isnull=False).order_by('due_date')
        
        # Calculate top positions for each task
        tasks_with_positions = []
        for index, task in enumerate(tasks):
            position = index * 160  # Adjust this value as needed
            tasks_with_positions.append({
                'task': task,
                'position': position,
            })

        return render(request, "todolist/today.html", {'tasks': tasks_with_positions})

class CreateTask(View):
    def get(self, request):
        # Get today's date
        today = timezone.now().date()
        # Retrieve tasks for today
        today_tasks = Tasks.objects.filter(due_date=today)
        
        # Render the form template with today's tasks in context
        return render(request, 'todolist/addtask.html', {'tasks': today_tasks})

    def post(self, request):
        # Manually retrieve form fields from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        starred = request.POST.get('starred') == 'on'
        priority = request.POST.get('priority')
        notes = request.POST.get('notes')
        completed = request.POST.get('completed') == 'on'
        overdue = request.POST.get('overdue') == 'on'
        category = request.POST.get('category')
        recurrence = request.POST.get('recurrence')

        # Convert due_date from string to a date object using the correct format
        due_date_obj = None
        if due_date:
            due_date_obj = timezone.datetime.strptime(due_date, '%Y-%m-%d').date()

        # Convert due_time from string to a time object
        due_time_obj = None
        if due_time:
            due_time_obj = timezone.datetime.strptime(due_time, '%H:%M').time()

        # Create a new instance of the model
        task = Tasks.objects.create(
            title=title,
            description=description,
            due_date=due_date_obj,
            due_time=due_time_obj,
            starred=starred,
            priority=priority,
            notes=notes,
            completed=completed,
            overdue=overdue,
            category=category,
            recurrence=recurrence,
        )

        # Redirect to today's task list
        return redirect('todolist:today')
class DeleteTask(View):
    def post(self, request, title):
        try:
            task_title = title.replace('-', ' ')  # Restore spaces in the title
            task = Tasks.objects.get(title=task_title)
            task.delete()
            return redirect('todolist:today')
        except Tasks.DoesNotExist:
            # Handle the case where the task does not exist
            return redirect('todolist:today')
class Starred(View):
    def get(self, request):
        return render(request, "todolist/starred.html")
    
class Schedule(View):
    def get(self, request):
        return render(request, "todolist/schedule.html")
    
    
class Completed(View):
    def get(self, request):
        return render(request, "todolist/completed.html")
    
class All(View):
    def get(self, request):
        return render(request, "todolist/all.html")
    
class Overdue(View):
    def get(self, request):
        return render(request, "todolist/overdue.html")