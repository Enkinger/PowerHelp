from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Post
        #fields = ["tipo", "correo", "nombre", "descripcion"]
        fields = '__all__'
