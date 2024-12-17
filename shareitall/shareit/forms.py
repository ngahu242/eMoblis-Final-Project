
from django import forms
from .models import Category, Listing, Service, ForumPost, Comment, Donation


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'location', 'image']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'contact_info']


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class DonationForm(forms.Form):
    donor_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    donor_phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter donation amount'}))