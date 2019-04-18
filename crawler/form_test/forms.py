from django import forms

class Contact_Us(forms.Form):
    name = forms.CharField(label='Youre name', max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
