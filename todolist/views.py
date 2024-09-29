from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Tasks
from django.utils import timezone
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



# Create your views here.\
class Today(View):
    def get(self, request):
        tasks = Tasks.objects.filter(due_date__isnull=False).order_by('due_date')
        return render(request, "todolist/today.html", {'tasks': tasks}) 
from django.views import View
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Tasks

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