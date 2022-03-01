
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'introduce/index.html')

def editor(request):
    return render(request, 'introduce/editor/editor.html')

def editor_content(request,content):
    if content == 'examples':
        return render(request,'introduce/editor/examples.html')
    elif content == 'practice':
        return render(request,'introduce/editor/practice.html')
    else:
        return HttpResponse('---非法请求---')
        
def entity(request):
    return render(request, 'introduce/entity/entity.html')

def entity_content(request,content):
    if content == 'examples':
        return render(request,'introduce/entity/examples.html')
    elif content == 'practice':
        return render(request,'introduce/entity/practice.html')
    else:
        return HttpResponse('---非法请求---')


def mate(request):
    return render(request, 'introduce/mate/mate.html')

def mate_content(request,content):
    if content == 'examples':
        return render(request,'introduce/mate/examples.html')
    elif content == 'practice':
        return render(request,'introduce/mate/practice.html')
    else:
        return HttpResponse('---非法请求---')

def semantic(request):
    return render(request, 'introduce/semantic/semantic.html')

def semantic_content(request,content):
    if content == 'examples':
        return render(request,'introduce/semantic/examples.html')
    elif content == 'practice':
        return render(request,'introduce/semantic/practice.html')
    else:
        return HttpResponse('---非法请求---')

def list(request):
    return render(request, "introduce/list/list.html")

def list_content(request,content):
    if content == 'examples':
        return render(request,'introduce/list/examples.html')
    elif content == 'practice':
        return render(request,'introduce/list/practice.html')
    else:
        return HttpResponse('---非法请求---')

def links(request):
    return render(request, "links.html")

def pciture(request):
    return render(request, "picture.html")

def inline(request):
    return render(request, "inline.html")

def multi(request):
    return render(request, "multi.html")

def editor_Examples(request):
    return render(request,'editor_Examples.html')