from django.urls import path 
from . import views

app_name = "users"

urlpatterns = [
    path('', views.Profile.as_view(), name="profile"),
    path('signup', views.Register.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
]
