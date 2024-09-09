from django.urls import path 
from . import views

app_name = 'thoughts'

urlpatterns = [
    path('', views.Thoughts.as_view(), name="thoughts")
]
