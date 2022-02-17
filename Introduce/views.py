
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'I_index.html')

def editor(request):
    return render(request, 'editor.html')

def entity(request):
    return render(request, 'entity.html')

def mate(request):
    return render(request, 'mate.html')

def semantic(request):
    return render(request, 'semantic.html')

def list(request):
    return render(request, "list.html")

def links(request):
    return render(request, "links.html")

def pciture(request):
    return render(request, "picture.html")

def inline(request):
    return render(request, "inline.html")

def multi(request):
    return render(request, "multi.html")