from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='base'),
    path('signup/', views.signup),
    path('logout/', views.logout_view),
    path('login/', views.login_view),
    path('edit/', views.edit_profile),
    path('orders/', views.orders)
]