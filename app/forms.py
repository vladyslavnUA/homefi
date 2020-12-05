from django import forms
from django.forms import ClearableFileInput
from .models import *

class ListingForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Listing 
        fields = "__all__"
        exclude = ['author']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }

class UpdateListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = "__all__"
        exclude = ['author']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }
    
    # def save(self, commit=True):
    #     listing = self.instance
    #     forum_post.title = self.cleaned_data['title']
    #     forum_post.body = self.cleaned_data['body']

    #     if self.cleaned_data['image']:
    #         forum_post.image = self.cleaned_data['image']
        
    #     if commit:
    #         forum_post.save()
    #     return forum_post