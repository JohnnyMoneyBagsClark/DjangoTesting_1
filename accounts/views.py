from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a login page, or home page, etc.
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home(request):
    return HttpResponse('Welcome to the home page!')