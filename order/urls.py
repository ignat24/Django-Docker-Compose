from . import views
from django.urls import path
urlpatterns = [
    path('', views.first_view),
    path('bad_users/', views.bad_users),

]