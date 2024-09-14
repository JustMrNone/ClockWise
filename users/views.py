from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile.html")
    
class Register(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "users/signup.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in the user after sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')  # Redirect to the profile page
        return render(request, "users/signup.html", {"form": form})

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        return render(request, "users/login.html", {"form": form})
