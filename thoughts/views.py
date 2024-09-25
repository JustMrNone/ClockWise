from django.shortcuts import render
from django.views import View 

# Create your views here.
class Thoughts(View):
    def get(self, request):
        return render(request, 'thoughts/dashboard.html')
    
class Write(View):
    def get(self, request):
        return render(request, 'thoughts/write.html')
    
class Library(View):
    def get(self, request):
        return render(request, 'thoughts/library.html')

class Categories(View): 
    def get(self, request):
        return render(request, 'thoughts/categories.html')

class Archived(View):
    def get(self, request):
        return render(request, 'thoughts/archived.html')