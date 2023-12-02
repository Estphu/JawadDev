from django import forms

class PostSearchForm(forms.Form):
    query = forms.CharField(required=False)