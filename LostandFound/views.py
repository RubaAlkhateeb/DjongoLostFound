from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# def index(request):
#     #template = loader.get_template('LostandFound/index.html')
#     return render(request, 'index.html',{})

# def Add(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = PostForm()

#     return render(request, 'Add.html',{'form':form})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'

class AddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add.html'
    #fields = '__all__'

    # def form_valid(self, form): 
    #     print(form.cleaned_data) 
    #     return super().form_valid(form) 

class ItemView(ListView):
    model = Post
    template_name = 'viewitem.html'
    ordering = ['-id']

class ItemDetail(DetailView):
    model = Post
    template_name = 'ItemDetail.html'

class DeleteItem(DeleteView):
    model = Post
    template_name = 'DeleteItem.html'
    success_url = reverse_lazy('viewitem')