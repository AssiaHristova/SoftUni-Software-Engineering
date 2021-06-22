from django.shortcuts import render, redirect

from books.books_app.forms import BookForm, StateFilterForm
from books.books_app.models import Book


def show_create_form(request, form):
    context = {'form': form}
    return render(request, 'create.html', context)


def show_update_form(request, form):
    context = {'form': form}
    return render(request, 'edit.html', context)


def index(request):
    state_form = StateFilterForm(request.GET)
    state_form.is_valid()
    state = state_form.cleaned_data['state']
    if state == 'all':
        books = Book.objects.all()

    context = {'books': Book.objects.all(), 'state_form': state_form}
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        return show_create_form(request, BookForm())
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_create_form(request, form)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(initial=book.__dict__)
        return show_update_form(request, form)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        return show_update_form(request, form)
