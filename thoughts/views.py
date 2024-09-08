from django.shortcuts import render
from django.views import View 

# Create your views here.
class Thoughts(View):
    def get(self, request):
        return render(request, 'thoughts/thoughts.html')