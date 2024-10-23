import requests
import os
# from django_project.settings import MAILGUN_API_KEY
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.views.generic import (
     ListView, 
     DetailView, 
     CreateView,
     UpdateView,
     DeleteView
     )
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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
    paginate_by = 7 # number of elments per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
      return render(request, 'blog/about.html', {'title':'About...'})

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

# def send_simple_message(request):
#     if request.method == 'POST':
#         email_to = request.POST.get('email_to')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Sending email using Mailgun API
#         response = requests.post(
#             "https://api.mailgun.net/v3/sandbox2bf5f20a05ef43bdad8033d96f8c97f5.mailgun.org/messages",
#             auth=("api", MAILGUN_API_KEY),
#             data={
#                 "from": "Excited User <mailgun@sandbox2bf5f20a05ef43bdad8033d96f8c97f5.mailgun.org>",
#                 "to": email_to,
#                 "subject": subject,
#                 "text": message
#             }
#         )

#         if response.status_code == 200:
#             return render(request, 'email_success.html')  # A success page
#         else:
#             return render(request, 'email_failure.html', {"error": response.text})  # A failure page

#     return(response) # Render the form if not POST



# def send_mail_page(request):
#     context = {}

#     if request.method == 'POST':
#         email_to = request.POST.get('email_to')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         if email_to and subject and message:
#             try:
#                 send_email_send_grid(email_to, subject, message)
#                 context['result'] = 'Email sent successfully'
#                 print(context)

#             except Exception as e:
#                 context['result'] = f'Error sending email: {e}'
#         else:
#             context['result'] = 'All fields are required'
    
#     return render(request, "blog/email_form.html", context)