from django.shortcuts import render, redirect
from ..models import Book

from django.http import HttpResponse
# Create your views here.

def homepage(request):
    if request.method=='POST':
        book_id = request.POST.get('bid')
        book_name = request.POST.get('bname')
        book_price = request.POST.get('bprice')
        book_qty = request.POST.get('bqty')
        book_published = request.POST.get('bpublished')
        if book_published=="Yes":
            book_published = True
        else:
            book_published = False

        if not book_id:
            book = Book(name=book_name, price=book_price, qty=book_qty, is_published=book_published)
            book.save()
            return redirect('show_books')
            # return HttpResponse("Book added Successfully..!")
        else:
            book_obj = Book.objects.get(id=book_id)
            book_obj.name = book_name
            book_obj.price = book_price
            book_obj.qty = book_qty
            book_obj.is_published = book_published
            book_obj.save()
            # return HttpResponse("Book updated Successfully..!")
            return redirect('show_books')

    else:
        return render(request, 'home.html')


def show_books(request):
    book_obj = Book.objects.all()
    data = {'all_books':book_obj}
    return render(request, 'show_books.html', data)

def edit_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    data = {'book':book_obj}
    return render(request, 'home.html', data)

def delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    if book_obj.is_published==True:
        book_obj.is_published = False
        book_obj.save()
    else:
        book_obj.delete()
    return redirect('show_books')

def restore_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    if book_obj.is_published==False:
        book_obj.is_published = True
        book_obj.save()
    return redirect('show_books') 

def show_published_books(request):
    book_obj = Book.objects.filter(is_published=True)
    data = {'all_books':book_obj}
    return render(request, 'show_books.html', data)


