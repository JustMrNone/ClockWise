from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Thoughts.as_view(), name="thoughts")
]
