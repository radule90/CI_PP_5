from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    '''
    Form for review and rating submitting
    '''
    class Meta:
        model = Review
        fields = ['subject', 'review', 'rating']
