from django import forms
from .models import Post
#from .settings import DATE_INPUT_FORMATS

class PostForm(forms.ModelForm):
    #Date = forms.DateField(input_formats='%d-%m-%Y')
    class Meta:
        model = Post
        fields = [
            'Item_Name',
            'Founder',
            'Contect_Information',
            'Date',
            'Description',
            'Image'
        ]

        widgets = {
            'Item_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Founder': forms.TextInput(attrs={'class':'form-control'}),
            'Contect_Information': forms.TextInput(attrs={'class':'form-control'}),
            'Date': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Image': forms.FileInput(attrs={'class':'form-control-file'}),
        }