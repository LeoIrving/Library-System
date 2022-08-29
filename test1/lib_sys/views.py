from django.shortcuts import render
from lib_sys.models import BookInfo,AuthorInfo,LenderInfo,BorrowerInfo
# Create your views here.

def show_books(request):
    books = BookInfo.objects.all()
    return render(request, 'lib_sys/show_books.html',{'books':books})

def detail(request, bid):
    book = BookInfo.objects.get(id = bid)
    return render(request, 'lib_sys/detail.html', {'book':book})

def show_authors(request):
    authors = AuthorInfo.objects.all()
    return render(request, 'lib_sys/show_authors.html', {'authors':authors})

def authorinfo(request, aid):
    author = AuthorInfo.objects.get(id = aid)
    books = author.bookinfo_set.all()
    return render(request, 'lib_sys/authorinfo.html',{'author':author, 'books': books})

def show_lenders(request):
    lenders = LenderInfo.objects.all()
    return render(request, 'lib_sys/show_lenders.html', {'lenders':lenders})

def lenderinfo(request, lid):
    lender = LenderInfo.objects.get(id = lid)
    books = lender.bookinfo_set.all()
    return render(request, 'lib_sys/lenderinfo.html',{'lender':lender, 'books': books})

def show_borrowers(request):
    borrowers = BorrowerInfo.objects.all()
    return render(request, 'lib_sys/show_borrowers.html', {'borrowers':borrowers})

def borrowerinfo(request, boid):
    borrower = BorrowerInfo.objects.get(id = boid)
    books = borrower.bookinfo_set.all()
    return render(request, 'lib_sys/borrowerinfo.html',{'borrower':borrower, 'books': books})