from django import forms
from django.forms import widgets 
from .models import Book , Review


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'write your review','class':'form-control','rows':5}))
    image = forms.ImageField(required=False) 

    class Meta:
        model = Review
        fields = ['review_text','image']
