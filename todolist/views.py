from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

# Create your views here.\
class Today(View):
    def get(self, request):
        return render(request, "todolist/today.html")
    
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