from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('',views.BookListView.as_view(),name='index'),

    # path('',views.index , name='index'),
    path('book/<str:pk>/detail',views.book_detail , name='book_detail'),
    path('book_review/<str:pk>/',views.book_review , name='book_review'),
]