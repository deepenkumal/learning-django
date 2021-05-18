from django.shortcuts import redirect, render
from .models import Book, Review
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    books = Book.objects.all()

    #search code
    search = request.GET.get('search-items')
    if search != '' and search is not None:
        books = Book.objects.filter(title__icontains=search)

    #paginator
    paginator = Paginator(books,4)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)

    return render(request, 'books/index.html',{'books':books})

def book_detail(request, pk):
    book = Book.objects.get(id = pk)
    reviews = book.review_set.all()
    context  = {
        'book':book,
        'reviews' : reviews,
    }
    return render(request ,'books/book_detail.html',context)

@login_required(login_url='users:login')
def book_review(request,pk):
    book = Book.objects.get(id= pk)
    review = request.POST.get('review')
    print(review)
    review = book.review_set.create(review_text= review, user_profile = request.user.userprofile)
    
    return redirect('books:index')
    