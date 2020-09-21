from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    #template = loader.get_template('LostandFound/index.html')
    return render(request, 'index.html',{})

def Add(request):
    #template = loader.get_template('LostandFound/index.html')
    return render(request, 'Add.html',{})

