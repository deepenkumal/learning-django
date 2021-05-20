from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('',views.BookListView.as_view(),name='index'),
    path('book/<str:pk>/detail',views.BookDetailView.as_view() , name='book_detail'),

    path('book_review/<str:pk>/',views.book_review , name='book_review'),
    path('author/<str:author>/',views.author , name='author'),
    path('search_book/',views.search_book, name='search_book'),
]