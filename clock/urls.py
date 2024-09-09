from django.urls import path 
from . import views

app_name = 'clock'

urlpatterns = [
    path("", views.Clock.as_view(), name="clock"),
    path("alarm", views.Alarm.as_view(), name="alarm"),
    path("stopwatch", views.StopWatch.as_view(), name="stopwatch"),
    path("pomodoro", views.Pomodoro.as_view(), name="pomodoro"),
    path("timer", views.Timer.as_view(), name="timer"),
    path("worldclock", views.WorldClock.as_view(), name="worldclock")
]
