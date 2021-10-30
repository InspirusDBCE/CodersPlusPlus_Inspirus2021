from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def SignUpView(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
    else:
        form = SignUpForm(None)
    return render(request, 'users/SignUp.html', {"form": form})