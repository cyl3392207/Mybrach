from django.shortcuts import render_to_response
from django.shortcuts import redirect


def index(request):
    return redirect(trending)

def trending(request):
    return render_to_response('trending.html')

def recent(request):
    return render_to_response('recent.html')
