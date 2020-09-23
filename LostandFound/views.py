from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

# def index(request):
#     #template = loader.get_template('LostandFound/index.html')
#     return render(request, 'index.html',{})

# def Add(request):
#     #template = loader.get_template('LostandFound/index.html')
#     return render(request, 'Add.html',{})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class AddView(ListView):
    model = Post
    template_name = 'Add.html'

class ItemView(DetailView):
    model = Post
    template_name = 'viewitem.html'
