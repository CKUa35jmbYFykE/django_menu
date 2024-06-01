# menu/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Order
from .forms import DishForm, UserRegistrationForm, OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def dish_list(request):
    dishes = Dish.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    return render(request, 'menu/dish_list.html', {'dishes': dishes, 'is_admin': is_admin})

def order_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        order = Order(dish=dish, user=request.user)
        order.save()
    else:
        return redirect('/')
    
    return render(request, 'menu/order_dish.html', {'dish': dish})

def admin_add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'menu/admin_add_dish.html', {'form': form})

def admin_order_list(request):
    orders = Order.objects.all()
    return render(request, 'menu/admin_order_list.html', {'orders': orders})

def order_confirmation(request):
    return render(request, 'order_confirmation.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dish_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')