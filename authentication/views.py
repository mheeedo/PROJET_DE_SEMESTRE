from authentication.models import Profile
from products.models import Product
from authentication.forms import UserRegisterForm
from django.shortcuts import redirect, render

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})




@login_required
def profile(request,id_profile):
    
    return render(request, 'authentication/profile.html',)


