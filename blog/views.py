from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.views.generic import (
     ListView, 
     DetailView, 
     CreateView
     )


def home(request):
    context = {
         'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
      return render(request, 'blog/about.html', {'title':'About...'})