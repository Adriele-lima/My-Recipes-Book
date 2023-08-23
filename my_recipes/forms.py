from django import forms
from .models import Post


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'ingredients_content', 
            'method_content']
