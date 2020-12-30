from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

default_permissions = [

]

def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)

            user.user_permissions.set(default_permissions)

            login(req, user)
            return redirect('invoices_app:invoices')
        else:
            return render(req, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(req, 'registration/register.html', {'form': form})
