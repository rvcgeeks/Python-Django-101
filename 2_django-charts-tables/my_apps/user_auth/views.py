
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages, auth
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode('utf-8')
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    messages.error(request, "Email or Password invalid!", "login_failure")
    return redirect('/')

def success(request):
    try:
        user = User.objects.get(id=request.session['id'])
    except KeyError:
        messages.error(request, "Please Login First!", "login_failure")
        return redirect('/') # if someone tries this url explicitly
    context = {
        "user": user
    }
    return render(request, 'success.html', context)

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
