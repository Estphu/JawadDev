from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea)