
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def editor(request):
    return render(request, 'HTML/editor.html')

def index(request):
    return render(request, 'HTML/I_index.html')


