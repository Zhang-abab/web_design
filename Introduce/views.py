<<<<<<< f4fc776c58b415edc252e933b892089ccaaede05
from turtle import ht
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
=======
from django.shortcuts import render
>>>>>>> Introduce


# Create your views here.
def editor(request):
<<<<<<< f4fc776c58b415edc252e933b892089ccaaede05
    return render(request, 'HTML/editor.html')

def index(request):
    return render(request, 'HTML/I_index.html')
=======
    return render(request, 'editor.html')
>>>>>>> Introduce


