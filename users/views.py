from django.shortcuts import render_to_response, redirect

def register(request):
    return render_to_response('users/register.html')

def login(request):
    return render_to_response('users/login.html')

def logout(request):
    return redirect(register)

def profile(request):
    pass