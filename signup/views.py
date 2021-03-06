from django.shortcuts import redirect, render
from .forms import RegisterForm
# Create your views here.

def register_view(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(response, "registration/signup.html", {"form": form})


