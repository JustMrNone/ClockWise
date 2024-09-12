from django.urls import path 
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.Today.as_view(), name="today"),
    path('starred', views.Starred.as_view(), name="starred"),
    path('schedule', views.Schedule.as_view(), name="schedule"),
    path('completed', views.Completed.as_view(), name="completed"),
    path('all', views.All.as_view(), name="all"),
    path('overdue', views.Overdue.as_view(), name="overdue")
]
