from django import forms
from django.forms import ModelForm
from .models import QuestionModel


class QuestionForm(ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['question_text', 'choice_text1', 'choice_text2', 'choice_text3']

        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'id': 'question_text'}),
            'choice_text1': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'choice_text1', 'placeholder': ' Choice 1'}),
            'choice_text2': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'choice_text2', 'placeholder': ' Choice 2'}),
            'choice_text3': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'choice_text3', 'placeholder': ' Choice 3'}),
        }
