from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account {username} has been created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.hml', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


from django.contrib.auth.views import LogoutView

def logout(request):
    if request.method == 'POST':
        messages.success(
            request, "Awesome! You have been logged out successfully!")
        return LogoutView.as_view(next_page='login')(request)
    else:
        return render(request, 'users/logout.html')