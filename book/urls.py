from . import views
from django.urls import path
urlpatterns = [
    path('', views.first_view, name='home'),
    path('author/', views.by_author),
    path('user/', views.by_user),
    path('detail/', views.detail, name='detail'),
    path('detail/<received_id>', views.detail, name='detail'),
    path('order/<book_id>', views.order, name='order'),
    path('unordered/', views.unordered),
    path('add_book/', views.AddPostView.as_view(), name='add_book'),
    path('update/<int:pk>', views.UpdateBookView.as_view(), name='update_book'),
    path('<int:pk>/delete', views.DeleteBookView.as_view(), name='delete_book')
]