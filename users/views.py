#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from product.views import index
from models import User

def register(request):
    context = {}
    if request.method == 'GET':
        context['next'] = request.GET.get('next', '')
        return render_to_response('users/register.html', context, RequestContext(request))

    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    next = request.POST.get('next', '')

    try:
        User.objects.create_user(username, email, password)
        user = authenticate(credential=username, password=password)
        auth_login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect(index)
    except Exception as ex:
        context['error'] = ex
        context['username'] = username
        context['email'] = email
        context['password'] = password
        context['next'] = next
        return render_to_response('users/register.html', context, RequestContext(request))


def login(request):
    context = {}
    if request.method == 'GET':
        context['next'] = request.GET.get('next', '')
        return render_to_response('users/login.html', context, RequestContext(request))

    credential = request.POST.get('credential', '')
    password = request.POST.get('password', '')
    next = request.POST.get('next', '')

    user = authenticate(credential=credential, password=password)
    if user:
        auth_login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect(index)
    else:
        context['error'] = u'密码错误'
        context['credential'] = credential
        context['next'] = next
        return render_to_response('users/login.html', context, RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect(index)

@login_required
def profile(request):
    return render_to_response('users/profile.html')

def reset_password(request):
    return HttpResponse(0)

def forget_password(request):
    return HttpResponse(0)

def check(request):
    return HttpResponse(0)