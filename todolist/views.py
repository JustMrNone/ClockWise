from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Tasks

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
        # Render the form template
        return render(request, 'todolist/addtask.html')

    def post(self, request):
        # Manually retrieve form fields from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        starred = request.POST.get('starred') == 'on'  # Checkbox returns 'on' when checked
        priority = request.POST.get('priority')
        notes = request.POST.get('notes')
        completed = request.POST.get('completed') == 'on'
        overdue = request.POST.get('overdue') == 'on'
        category = request.POST.get('category')
        recurrence = request.POST.get('recurrence')

        # Convert due_date from string to a date object
        due_date_obj = None
        if due_date:
            due_date_obj = timezone.datetime.strptime(due_date, '%B %d, %Y').date()  # Adjust format if needed

        # Create a new instance of the model manually
        task = Tasks.objects.create(
            title=title,
            description=description,
            due_date=due_date_obj,  # Save the date object
            due_time=due_time,
            starred=starred,
            priority=priority,
            notes=notes,
            completed=completed,
            overdue=overdue,
            category=category,
            recurrence=recurrence,
        )

        # After saving, redirect to some other view (e.g., task list)
        return redirect('task_list')

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