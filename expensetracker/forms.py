from django import forms
from .models import ExpenseProfile

class ExpenseProfileVerifyForm(forms.Form):

    QUESTIONS = (
    ('What was the name of your first pet?', 'What was the name of your first pet?'),
    ('In which city or town were you born?', 'In which city or town were you born?'),
    ('What is the title of your favorite book or movie?', 'What is the title of your favorite book or movie?'),
    ('What is the name of the city where you attended your first concert?', 'What is the name of the city where you attended your first concert?'),
    ('Who is your favorite author or film director?', 'Who is your favorite author or film director?')
    )

    username = forms.CharField(max_length=60)
    question = forms.ChoiceField(choices=QUESTIONS)
    answer = forms.CharField(max_length=60)

    def clean(self):
        cleaned_data = super().clean()

        username_value = cleaned_data.get('username')
        question_value = cleaned_data.get('question')
        answer_value = cleaned_data.get('answer')
        print(username_value)

        # Example: Custom validation with existing values in the model
        existing_objects = ExpenseProfile.objects.filter(username=username_value, question=question_value, answer=answer_value)

        
        self.errors.pop('username', None)

        if existing_objects.exists():
            # If values exist, consider the form valid and redirect to the next page
            return cleaned_data
        
        # If values don't exist, add an error to the form
        self.add_error(None, 'The specified combination does not exist.')

        # Add more custom validation or modify cleaned_data as needed
        return cleaned_data