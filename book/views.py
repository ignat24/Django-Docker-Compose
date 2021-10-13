from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Book
from authentication.models import CustomUser
from author.models import Author
from order.models import Order
from .forms import QueryForm, UserForm, BookIDForm, SortFilterForm, BookForm, BookFormUpdate, OrderForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta


def first_view(request):
    form = SortFilterForm(request.GET)
    books = Book.objects.all()
    query_filter = request.GET.get('filter')
    if query_filter:
        to_find = request.GET.get('find')
        if to_find:
            if query_filter == '1':
                books = books.filter(authors__id__contains=to_find)
            elif query_filter == '2':
                books = books.filter(count=int(to_find))
            elif query_filter == '3':
                books = books.filter(name__contains=to_find)
            elif query_filter == '4':
                books = books.filter(description__contains=to_find)
    query_sort = request.GET.get('sort')
    if query_sort:
        if query_sort == '1':
            books = sorted(
                books,
                key=lambda x: x.name, reverse=False
            )
        elif query_sort == '2':
            books = sorted(
                books,
                key=lambda x: x.name, reverse=True
            )
        elif query_sort == '3':
            books = sorted(
                books,
                key=lambda x: x.count, reverse=False
            )
        elif query_sort == '4':
            books = sorted(
                books,
                key=lambda x: x.count, reverse=True
            )

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main.html', {'page_obj': page_obj, 'form': form})


def by_author(request):
    query = request.GET.get('author_id')
    if query:
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            author_id = form.cleaned_data['author_id']
            author = Author.get_by_id(author_id)
            if author is None:
                return HttpResponse('There are no such author')
            books = Book.get_by_author(author_id)
            paginator = Paginator(books, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'author.html', {'page_obj': page_obj, 'author': author, 'form':form})
        # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm()
        books = Book.get_all()
        paginator = Paginator(books, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'author.html', {'page_obj': page_obj, 'form':form})


def by_user(request):
    query = request.GET.get('user_id')
    if query:
        # create a form instance and populate it with data from the request:
        form = UserForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            user_id = form.cleaned_data['user_id']
            user = CustomUser.get_by_id(user_id)
            if user is None:
                return HttpResponse('There are no such user')
            books = Order.get_books_by_user(user_id)
            paginator = Paginator(books, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'user.html', { 'user': user, 'form': form, 'page_obj': page_obj})
        # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
        books = Book.get_all()
        paginator = Paginator(books, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'user.html', {'form': form, 'page_obj': page_obj})


def detail(request, received_id=None):
    if received_id:
        form = BookIDForm()
        book = Book.get_by_id(received_id)
        if book is None:
            return HttpResponse('There are no such book')
        return render(request, 'detail.html', {'book': book, 'form': form})
    else:
        query = request.GET.get('book_id')
        if query:
            # create a form instance and populate it with data from the request:
            form = BookIDForm(request.GET)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                book_id = form.cleaned_data['book_id']
                book = Book.get_by_id(book_id)
                if book is None:
                    return HttpResponse('There are no such book')
                return render(request, 'detail.html', {'book': book, 'form': form})
            # if a GET (or any other method) we'll create a blank form
        else:
            form = BookIDForm()
            return render(request, 'detail.html', {'form': form})


def unordered(request):
    books = Book.objects.exclude(id__in=[x.book.id for x in Order.objects.all()])
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'unordered.html', {'page_obj': page_obj})


def order(request, book_id):
    book = Book.get_by_id(book_id)
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            day = form.cleaned_data['day']
            Order.create(user=user, book=book, plated_end_at=timezone.now() + timedelta(days=int(day)))
            book.count -= 1

            return HttpResponseRedirect('/orders')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form, 'book': book})


class AddPostView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    

class UpdateBookView(UpdateView):
    model=Book
    form_class = BookFormUpdate
    template_name = 'update_book.html'

class DeleteBookView(DeleteView):
    model=Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('home')