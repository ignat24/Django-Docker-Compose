from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import CustomUserCreationForm, LoginForm, CustomUserUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order


def index(request):
    return render(request,'base.html',{})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def orders(request):
    orders = Order.get_by_user(request.user.id)
    return render(request, 'user_orders.html', {'orders': orders})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/edit')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm(instance=request.user)

    return render(request, 'edit.html', {'form': form})
