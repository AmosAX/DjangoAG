from django.shortcuts import render, redirect
## OBS VI MÅSTE IMPORTERA REDIRECT
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
#Finns många olika typer av messages värt att kolla upp!

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('base-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})