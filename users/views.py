from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from users.forms import UserProfileForm, UseForm


# Create your views here.


def register(request):
    form_user = UseForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UseForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            
            return redirect('home')
            
    context = {
        'form_user' : form_user,
        'form_profile' : form_profile,
        
    }
    
    return render(request, context)
    
def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, {'form': form})

    