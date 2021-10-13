from django.urls import path
from .views import *

urlpatterns = [
    path('login/',log_in, name='log_in'),
    path('create/',sign_up, name = 'sign_up'),

]