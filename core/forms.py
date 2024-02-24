from .models import *
from django import forms 







class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']

        widgets = {
            'name':forms.TextInput(attrs = {
                'class': 'name',
                'placeholder': 'Name'
            }),
            'email':forms.TextInput(attrs = {
                'class': 'f-email',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'textarea',
                'cols':30 ,
                'rows':15,
                'placeholder':'Type your message'
            })
        }
