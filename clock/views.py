from django.shortcuts import render
from django.views import View 

# Create your views here.


class Clock(View):
    def get(self, request):
        return render(request, "clock/clock.html")
    
class Alarm(View):
     def get(self, request):
         return render(request, "clock/alarm.html")
     
     
class Pomodoro(View):
    def get(self, request):
        return render(request, "clock/pomodoro.html")
    
class StopWatch(View):
    def get(self, request):
        return render(request, "clock/stopwatch.html")
    

class Timer(View):
    def get(self, request):
        return render(request, "clock/timer.html")
    
class WorldClock(View):
    def get(self, request):
        return render(request, "clock/worldclock.html")
    
