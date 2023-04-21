from django.shortcuts import render,redirect
from .models import Book,Author
from .forms import BookFormSet,BookForm
from django.http.response import HttpResponse

# Create your views here.

def create_book(request,pk):

    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail_book",pk=book.id)
        else:
            return render(request,"partials/book_form.html",{"form":form})
        
    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request,"create_book.html",context)

def index(request):
    return render(request,"index.html")

def create_book_form(request):
    context= {
        "form": BookForm()
    }
    return render(request,"partials/book_form.html",context)

def detail_book(request,pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "partials/detail_book.html", context)

def delete_book(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')

def update_book(request,pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None,instance=book)

    if request.method == "POST":
        if form.is_valid():
            book = form.save()
            return redirect("detail_book",pk=book.id)

    context = {
        "form":form,"book":book
    }
    return render(request,"partials/book_form.html",context)