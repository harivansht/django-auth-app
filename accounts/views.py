from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm, PasswordChangeCustomForm
from .models import User

# Signup


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Login


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('dashboard')
        messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Forgot Password


def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(from_email='support@example.com', request=request,
                      email_template_name='accounts/password_reset_email.html')
            messages.success(
                request, 'Password reset link sent to your email.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/forgot_password.html', {'form': form})

# Change Password


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('dashboard')
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

# Dashboard


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Profile


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# Logout


def logout_view(request):
    logout(request)
    return redirect('login')
