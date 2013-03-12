from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

def register(request):
    return render_to_response('users/register.html')

def login(request):
    return render_to_response('users/login.html')

def logout(request):
    return redirect(register)

def profile(request):
    return render_to_response('users/profile.html')

def reset_password(request):
    return HttpResponse(0)

def forget_password(request):
    return HttpResponse(0)

def check(request):
    return HttpResponse(0)