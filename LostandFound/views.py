from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
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

class AddView(CreateView):
    model = Post
    template_name = 'Add.html'
    fields = '__all__'

class ItemView(ListView):
    model = Post
    template_name = 'viewitem.html'

class ItemDetail(DetailView):
    model = Post
    template_name = 'ItemDetail.html'
