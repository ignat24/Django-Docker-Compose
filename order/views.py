from django.shortcuts import render
from .models import Order
from authentication.models import CustomUser
from django.core.paginator import Paginator
from django.utils import timezone


def first_view(request):
    orders = sorted(
        Order.get_all(),
        key=lambda x: x.plated_end_at, reverse=True
    )
    paginator = Paginator(orders, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders.html', {'page_obj': page_obj})

def bad_users(request):
    users = list(set([x.user for x in Order.objects.filter(plated_end_at__lte=timezone.now())]))
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bad_users.html', {'page_obj': page_obj})
