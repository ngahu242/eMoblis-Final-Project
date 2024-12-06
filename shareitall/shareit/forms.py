
from django import forms
from .models import Category, Listing, Service, ForumPost, Comment


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

