from django import forms 
from .models import Book , Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'



        