from django.shortcuts import redirect, render, resolve_url
from .models import Book, Review, Author
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import generic
from . forms import ReviewForm
from django.core.files.storage import FileSystemStorage



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
        context['form'] = ReviewForm()
        return context

    #bydefault looks for book_detail.html
    #bydefault context name is book


@login_required()
def book_review(request,pk):
    if request.method == 'POST':
        new_review = Review(book_id=pk,userprofile=request.user.userprofile)
        form = ReviewForm(request.POST,request.FILES,instance=new_review)
        if form.is_valid():
            form.save()

    return redirect(f'/book/{pk}/detail')
    


    # book = Book.objects.get(id= pk)
    # review = request.POST.get('review_text')
    # image = request.FILES.get('image')
    # book.review_set.create(review_text=review, userprofile = request.user.userprofile)

    # if image:
    #     fs = FileSystemStorage()
    #     name= fs.save(image.name, image)
    #     book.review_set.create(review_text=review, userprofile = request.user.userprofile,image = fs.url(name))
    # return redirect(f'/book/{pk}/detail')
    

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