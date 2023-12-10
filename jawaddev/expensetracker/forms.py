from django import forms
from .models import ExpenseProfile

class ExpenseProfileForm(forms.ModelForm):

    class Meta:
        model = ExpenseProfile
        fields = ['username', 'question', 'answer']

    def clean(self):
        cleaned_data = super().clean()

        username_value = cleaned_data.get('username')
        question_value = cleaned_data.get('question')
        answer_value = cleaned_data.get('answer')

        # Example: Custom validation with existing values in the model
        existing_objects = ExpenseProfile.objects.filter(username=username_value, question=question_value, answer=answer_value)

        if existing_objects.exists():
            # If values exist, consider the form valid and redirect to the next page
            return cleaned_data

        # If values don't exist, add an error to the form
        self.add_error(None, 'The specified combination does not exist.')

        # Add more custom validation or modify cleaned_data as needed
        return cleaned_data    