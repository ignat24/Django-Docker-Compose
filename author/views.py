from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorForm
from django.urls import reverse_lazy



# def home(request):
#     return render(request, 'main.html')

class AuthorsHomeView(ListView):
    model=Author
    context_object_name = 'authors'
    # queryset = Author.objects.all()
    template_name = 'main_authors.html'

class AddAuthorView(CreateView):

    model = Author
    form_class = AuthorForm
    template_name = 'add_author.html'

class EditAuthorView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'edit_author.html'


class DeleteAuthorView(DeleteView):
    context_object_name = 'author'
    model = Author
    form_class = AuthorForm
    template_name = 'delete_author.html'
    success_url = reverse_lazy('author_home')

