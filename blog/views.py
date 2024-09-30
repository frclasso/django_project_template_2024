from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

#dummy data
# posts = [
#      {
#           'author': 'Fabio Classo',
#           'title': 'Blog post 1',
#           'content': 'First post content',
#           'date_posted': datetime.now()
#      },
#      {
#           'author': 'Jane Doe',
#           'title': 'Blog post 2',
#           'content': 'Second post content',
#           'date_posted': datetime.now()
#      }
# ]


def home(request):
    context = {
         'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
      return render(request, 'blog/about.html', {'title':'About...'})