from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView,
                                       PasswordResetDoneView)
from django.contrib.auth.mixins import LoginRequiredMixin

# ----------function_view-----------------------


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(
                request=request, message=f'account is created for {username}, you are now able to log in')
            return redirect(to='user-login')
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='user/register.html', context={'form': form})


@login_required
def profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request=request, message=f'Your account has been updated !')
            resp = reverse('user-profile', args=[username, ])
            return redirect(resp)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request=request, template_name='user/profile.html', context={'u_form': u_form, 'p_form': p_form, })

# ------------------class_view-------------------------


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user/password_reset_complete.html'
