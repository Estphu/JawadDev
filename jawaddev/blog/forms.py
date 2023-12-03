from django import forms

class PostSearchForm(forms.Form):
    q = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': "Enter keywords and press 'Enter'", 'class': 'form-control w-100'}))