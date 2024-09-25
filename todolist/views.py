from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Tasks

# Create your views here.\
class Today(View):
    def get(self, request):
        tasks = Tasks.objects.filter(due_date__isnull=False).order_by('due_date')
        return render(request, "todolist/today.html", {'tasks': tasks}) 

class CreateTask(View):
    def get(self, request):
        return render(request, 'todolist/addtask.html')  # Render the task creation form

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', None)  # Handle this if you have a date field
        due_time = request.POST.get('due_time', None)  # Handle this if you have a time field

        # Create the task instance
        task = Tasks(
            title=title,
            description=description,
            due_date=due_date if due_date else None,
            due_time=due_time if due_time else None,
        )
        task.save()

        return redirect('todolist:today')  # Redirect to the today view after saving
    
    
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