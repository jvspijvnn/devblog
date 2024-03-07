from django import forms
from .models import commentaire


class CommentForm(forms.ModelForm):
    class Meta:
        model = commentaire
        fields = ['objet','content']
        widgets = {
           'objet':  forms.TextInput(attrs={'class': 'form'}),
           'content': forms.Textarea(attrs={'class': 'form-area'}),

       }

