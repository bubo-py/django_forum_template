from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('username')
            messages.success(request, f"created account for {new_user}")
            return redirect('index')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
