from django.shortcuts import render_to_response
from django.shortcuts import redirect

def index(request):
    return redirect(list_trending)

def list_trending(request):
    return render_to_response('trending.html')

def list_recent(request):
    return render_to_response('recent.html')

def list_popular(request):
    return render_to_response('popular.html')

def detail_product(request, product_id):
    return render_to_response('product.html')

def detail_save(request, product_id, save_id):
    return render_to_response('save.html')