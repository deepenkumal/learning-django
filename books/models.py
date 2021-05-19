from django.db import models
from users.models import UserProfile
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name = 'Author Name')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 256, verbose_name = 'Book Title ')
    author = models.ManyToManyField(Author)
    price = models.FloatField(verbose_name='Book Price')
    image = models.CharField(verbose_name='Book Image',max_length=256 ,null=True)
    description = models.CharField(max_length=256)
    long_description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    review_text = models.TextField(null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile ,on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_text

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[str(self.id)])
