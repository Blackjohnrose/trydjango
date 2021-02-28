from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Your account has been creted ! ')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_view(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profileuser)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)
