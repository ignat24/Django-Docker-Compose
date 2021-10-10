from book.views import UpdateBookView
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', AuthorsHomeView.as_view() , name='author_home'),
    path('update/<int:pk>', EditAuthorView.as_view() , name='author_update'),
    path('<int:pk>/delete/',DeleteAuthorView.as_view() , name='author_delete'),
    path('create/',AddAuthorView.as_view() , name='author_add')
]