from django.shortcuts import render,redirect

#ONÖDIG RAD, HAR DEN SOM MINNE
from django.contrib.auth.forms import UserCreationForm


#LITE TYDLIGARE MEN KAN DRA IMPORT ALL OM MAN VILL SPARA PÅ RADER
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

from django.contrib.auth.decorators import login_required


# Create your views here.

#HÄR SKALL VI KONTROLLERA OM VI FÅR ETT POST ANROP
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('list-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/reg.html', {'form': form})

@login_required
def profile(request):

    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request,'users/profile.html',context)