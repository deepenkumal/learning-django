from django.shortcuts import redirect, render, resolve_url
from .models import Book, Review, Author
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import generic



# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4

    template_name = 'books/index.html'
    
    
class BookDetailView(generic.DetailView):
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-review_date')
        context['authors'] = context['book'].author.all()
        return context

    #bydefault looks for book_detail.html
    #bydefault context name is book


@login_required()
def book_review(request,pk):
    book = Book.objects.get(id= pk)
    review = request.POST.get('review')
    if review != '' and review is not None:
        review = book.review_set.create(review_text= review, userprofile = request.user.userprofile)
    
    return redirect('books:index')
    

def author(request,author):
    books = Book.objects.filter(author__name = author)
    print(books)
    return render(request,'books/author.html',{'book_list':books, 'author':author})

##search code

def search_book(request):
    search_books =request.GET.get('search')
    print(search_books)
    if search_books != '' and search_books is not None:
        books = Book.objects.filter(title__icontains = search_books)
    return render(request,'books/index.html',{'book_list':books})