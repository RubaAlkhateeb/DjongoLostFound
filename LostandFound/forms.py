from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'Item_Name',
            'Founder',
            'Contect_Information',
            # 'Date',
            'Description',
            # 'Image'
        ]

        widgets = {
            'Item_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Founder': forms.TextInput(attrs={'class':'form-control'}),
            'Contect_Information': forms.TextInput(attrs={'class':'form-control'}),
            # 'Date',
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            # 'Image'
        }